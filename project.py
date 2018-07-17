from flask import (Flask,
                   render_template,
                   request, redirect,
                   url_for,
                   flash,
                   jsonify)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import (Base,
                            Dramas,
                            DramaLang,
                            User,
                            LatestDramas,
                            LatestDramaLang)

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = 'Dramas Application'

engine = create_engine('sqlite:///dramas.db',
                       connect_args={'check_same_thread': False},
                       echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/logout')
def showLogout():
    login_session.pop('username', None)
    return redirect(url_for('showDramas'))


@app.route('/gconnect', methods=['POST'])
def gconnect():
    print "gconnect-----------"
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json',
                                             scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print "Milestone 1"

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    print "The access token is valid for this app"

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        print "Oh oh... Current user is already connected."
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    print "Access token successfully stores in the session for later use."

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    print "User info successfully recovered."
    data = answer.json()
    print "User info recovered from Google API: %s" % data
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    user_id = getUserID(login_session['email'])
    login_session['user_id'] = user_id
    print "login_session: %s" % login_session
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    print 'In gdisconnect access token is %s', access_token
    print login_session.keys()
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token\
        =%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps
                                 ('Failed to revoke token for given user.',
                                  400))
        response.headers['Content-Type'] = 'application/json'
        return response


def createUser(login_session):
    newUser = User(name=login_session['user_id'],
                   email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email'])\
        .one_or_none()
    return user_id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).all()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one_or_none()
        return user.id
    except Exception:
        return None


@app.route('/dramas/<int:dramas_id>/dramasCat/JSON')
def dramaListJSON(dramas_id):
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    dlist = session.query(DramaLang).filter_by(dramas_id=dramas_id).all()
    return jsonify(DramaLang=[i.serialize for i in dlist])


@app.route('/dramas/<int:dramas_id>/dramasCat/<int:dramaLang_id>/JSON')
def dramaLangJSON(dramas_id, dramaLang_id):
    dramaLang = session.query(DramaLang).filter_by(id=dramaLang_id)\
        .one_or_none()
    return jsonify(DramaLang=dramaLang.serialize)


@app.route('/')
@app.route('/dramas/')
def showDramas():
    dramas = session.query(Dramas).all()
    dramaLang = session.query(DramaLang).all()
    return render_template('dramasCat.html', dramas=dramas)


@app.route('/dramas/new/', methods=['GET', 'POST'])
def newDramasCat():
    """
    this will create new drama category
    """
    if 'username' not in login_session:
        return redirect('/login/')
    if request.method == 'POST':
        newDramasCat = Dramas(name=request.form['name'],
                              user_id=login_session['user_id'])
        session.add(newDramasCat)
        flash('New Drama Category %s Successfully Created' % newDramasCat.name)
        session.commit()
        return redirect(url_for('showDramas'))
    else:
        return render_template('newDramasCat.html')


@app.route('/dramas/<int:dramas_id>/edit/', methods=['GET', 'POST'])
def editDramasCat(dramas_id):
    """
    this will edit any drama category
    """
    editedDramasCat = session.query(Dramas).filter_by(id=dramas_id)\
        .one_or_none()
    if 'username' not in login_session:
        return redirect('/login/')
    if editedDramasCat.user_id != login_session['user_id']:
        return "<script> function myFunction() {alert('You are not authorised\
        to edit this drama.Please createyour own drama in order to edit.'); }\
        </script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedDramasCat.name = request.form['name']
            flash('Drama Category Successfully Edited %s'
                  % editedDramasCat.name)
            return redirect(url_for('showDramas'))
    else:
        return render_template('editDRamasCat.html', dramas=editedDramasCat)


@app.route('/dramas/<int:dramas_id>/delete/', methods=['GET', 'POST'])
def deleteDramasCat(dramas_id):
    """
    this will delete any drama category
    """
    dramasCatToDelete = session.query(Dramas).filter_by(id=dramas_id)\
        .one_or_none()
    if 'username' not in login_session:
        return redirect('/login/')
    if dramasCatToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not\
        authorized to delete this drama. Please create your own drama\
        in order to delete.'); } </script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(dramasCatToDelete)
        flash('%s Successfully Deleted' % dramasCatToDelete.name)
        session.commit()
        return redirect(url_for('showDramas', dramas_id=dramas_id))
    else:
        return render_template('deleteDramasCat.html',
                               dramas=dramasCatToDelete)


@app.route('/dramas/latest/')
def showLatestDramas():
    """
    this will show latest dramas
    """
    latestDramas = session.query(LatestDramas).all()
    ldlist = session.query(LatestDramaLang).all()
    return render_template('latestDramas.html',
                           latestDramas=latestDramas, ldlist=ldlist)


# @app.route('/')
@app.route('/dramas/<int:dramas_id>/')
@app.route('/dramas/<int:dramas_id>/dramasCat/')
def dramaList(dramas_id):
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    #creator = getUserInfo(dramas.user_id)
    dlist = session.query(DramaLang).filter_by(dramas_id=dramas_id)
    return render_template('drama.html', dlist=dlist,
                               dramas=dramas)


@app.route('/dramas/<int:dramas_id>/dramasCat/new/', methods=['GET', 'POST'])
def newDramas(dramas_id):
    """
    this will create new drama in a particular drama category
    """
    if 'username' not in login_session:
        return redirect('/login/')
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    if login_session['user_id'] != dramas.user_id:
        return "<script> function myFunction() {alert('You are not authorized\
        to add to this drama.Please create your own drama in order to add.\
        '); }</script> <body onload = 'myFunction()''>"
    if request.method == 'POST':
            newDrama = DramaLang(name=request.form['name'],
                                 description=request.form['description'],
                                 genre=request.form['genre'],
                                 running_time=request.form['running_time'],
                                 no_of_episodes=request.form['no_of_episodes'],
                                 dramas_id=dramas_id, user_id=dramas.user_id)
            session.add(newDrama)
            session.commit()
            flash("New Drama: %s Successfully Created!" % (newDrama.name))
            return redirect(url_for('dramaList', dramas_id=dramas_id))
    else:
        return render_template('newdramas.html', dramas_id=dramas_id)


@app.route('/dramas/<int:dramas_id>/dramasCat/<int:dramaLang_id>/edit/',
           methods=['GET', 'POST'])
def editDramas(dramas_id, dramaLang_id):
    """
    this will edit any drama in a particular drama category
    """
    if 'username'not in login_session:
        return redirect('/login/')
    editedDrama = session.query(DramaLang).filter_by(id=dramaLang_id)\
        .one_or_none()
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    if login_session['user_id'] != dramas.user_id:
        return "<script>function myFunction() {alert('You are not\
        authorized to edit dramas information to this drama.Please\
        create your own drama in order to edit info.'); }</script><body\
        onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedDrama.name = request.form['name']
        if request.form['description']:
            editedDrama.description = request.form['description']
        if request.form['genre']:
            editedDrama.genre = request.form['genre']
        if request.form['running_time']:
            editedDrama.running_time = request.form['running_time']
        if request.form['no_of_episodes']:
            editedDrama.no_of_episodes = request.form['no_of_episodes']
        session.add(editedDrama)
        session.commit()
        flash("%s Successfully Edited!" % (editedDrama.name))
        return redirect(url_for('dramaList', dramas_id=dramas_id))
    else:
        return render_template('editdramas.html', dramas_id=dramas_id,
                               dramaLang_id=dramaLang_id,
                               item=editedDrama)


@app.route('/dramas/<int:dramas_id>/dramasCat/<int:dramaLang_id>/delete/',
           methods=['GET', 'POST'])
def deleteDramas(dramas_id, dramaLang_id):
    """
    this will delete any drama in a particular drama category
    """
    if 'username' not in login_session:
        return redirect('/login/')
    dramas = session.query(Dramas).filter_by(id=dramas_id).one_or_none()
    dramaToDelete = session.query(DramaLang).filter_by(id=dramaLang_id)\
        .one_or_none()
    if login_session['user_id'] != dramas.user_id:
        return " <script> function myFunction() {alert('You are not authorized\
        to delete information to this drama.Please create your own drama\
        in order to delete info.'); }</script><body onload='myFunction()''> "
    if request.method == 'POST':
        session.delete(dramaToDelete)
        session.commit()
        flash("%s Successfully Deleted!" % (dramaToDelete.name))
        return redirect(url_for('dramaList', dramas_id=dramas_id))
    else:
        return render_template('deletedramas.html', item=dramaToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
