import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """
    Registered user information is stored in db
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Dramas(Base):
    """
    Drama Categories' information is stored in db
    """
    __tablename__ = 'dramas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            }


class DramaLang(Base):
    """
    Dramas in that categories' information is stored in db
    """
    __tablename__ = 'dramas_lang'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    genre = Column(String(250))
    running_time = Column(String(10))
    no_of_episodes = Column(String(250))
    dramas_id = Column(Integer, ForeignKey('dramas.id'))
    dramas = relationship(Dramas)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'genre': self.genre,
            'running_time': self.running_time,
            'no_of_episodes': self.no_of_episodes,
            }


class LatestDramas(Base):
    """
    Latest dramas' information is stored in db
    """
    __tablename__ = 'latestDramas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            }


class LatestDramaLang(Base):
    """
    The latest dramas' detailed information is stored in db
    """
    __tablename__ = 'latestDramaLang'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    genre = Column(String(250))
    running_time = Column(String(10))
    no_of_episodes = Column(String(250))
    latestDramas_id = Column(Integer, ForeignKey('latestDramas.id'))
    latestDramas = relationship(LatestDramas)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'genre': self.genre,
            'running_time': self.running_time,
            'no_of_episodes': self.no_of_episodes,
            }


engine = create_engine('sqlite:///dramas.db')
Base.metadata.create_all(engine)
