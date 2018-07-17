from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Dramas, DramaLang, User, LatestDramas, LatestDramaLang

engine=create_engine('sqlite:///dramas.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

User1=User(name="Rumeet Rakhra",email="rumeetrakhra@gmail.com")
session.add(User1)
session.commit()

drama1=Dramas(user_id=1,name="KDramas")
session.add(drama1)
session.commit()

dramalang1=DramaLang(name="Descendants of the Sun",
                     description="""This story tells of doctors stationed in
                     the fictional war zone of Urk (Uruk), and follows the love
                     that develops between a surgeon (Kang Mo-yeon) and a
                     special forces officer (Yoo Shi-jin), both elite in their
                     respective fields. The story will track both their personal
                     and professional struggles while exploring issues about the value of life.""",
                     genre = "Romance, melodrama,comedy",
                     running_time="60 minutes",
                     no_of_episodes="16 + 3 Special Episodes",
                     dramas=drama1)
session.add(dramalang1)
session.commit()

dramalang2=DramaLang(name="W-Two Worlds Apart",
                     description="""A mysterious melodrama about a parallel universe which depicts
                     a man and a woman who live in the same Seoul but in different environments.""",
                     genre=" Romance, comedy, suspense, melodrama",
                     running_time="60 minutes",
                     no_of_episodes="16",
                     dramas=drama1)
session.add(dramalang2)
session.commit()

dramalang3=DramaLang(name="Legend of the Blue Sea",
                     description="""The television series centers on the love story of
                     Heo Joon-jae (Lee Min-ho), the son of a rich businessman who becomes a handsome and
                     clever con-man after his parents' divorce, and a mermaid named Shim Cheong (Jun Ji-hyun).
                     Focusing on rebirth, fate, and unrequited love, their tale is juxtaposed with the parallel
                     story of their Joseon era incarnations, town head Kim Dam-ryeong and the mermaid Se-hwa.""",
                     genre=" Romance, comedy, fantasy",
                     running_time="60 minutes",
                     no_of_episodes="20 + 1 Special",
                     dramas=drama1)
session.add(dramalang3)
session.commit()

dramalang4=DramaLang(name="Uncontrollably Fond",
                     description="""Noh Eul and Joon Young were forced to separate when they were young.
                     After some years both of them meet again, Noh Eul had become a documentary producer
                     and Joon Young is now a top singer and actor.""",
                     genre=" Melodrama, romance, comedy",
                     running_time="60 minutes",
                     no_of_episodes="20",
                     dramas=drama1)
session.add(dramalang4)
session.commit()

dramalang5=DramaLang(name="The K2",
                     description="""Drama about a patriotic bodyguard who was abandoned by his country and colleagues, a shut-in daughter of leading Presidential
                     candidate who regards love as a tool for revenge, and the First Lady contender who hides her ambition and charisma behind a kind and
                     friendly personality.""",
                     genre=" Melodrama, political, action",
                     running_time="60 minutes",
                     no_of_episodes="16",
                     dramas=drama1)
session.add(dramalang5)
session.commit()

dramalang6=DramaLang(name="My Love from the Star",
                     description="""Do Min Joon is an alien who was stranded four hundred years ago on Earth. He has cynical views on humans but when he gets
                     entangled in the life of a former actress, his opinion slowly changes.""",
                     genre = "Romance, comedy, fantasy, melodrama, thriller",
                     running_time="60 minutes",
                     no_of_episodes="21",
                     dramas=drama1)
session.add(dramalang6)
session.commit()

dramalang7=DramaLang(name="The Heirs",
                     description="""A romantic comedy about high school students living in top 1% high society, learning about love and friendship.
                     Things get turned topsy turvy when the students end up getting tangled
                     with a girl from lower class who is the heir of "poverty", and romance unfolds.""",
                     genre = "Romance, youth, school, melodrama, comedy",
                     running_time="60 minutes",
                     no_of_episodes="20",
                     dramas=drama1)
session.add(dramalang7)
session.commit()

dramalang8=DramaLang(name="Suspicious Partner",
                     description="""Noh Ji Wook, a prosecutor, met Eun Bong Hee, a 1st year judicial trainee for the first time in unexpected embarassing
                     incident. Three months later, they meet again as a supervisor and probationer. Things getting
                     worse when Bong Hee suddenly gets caught as a suspect for her ex-boyfriend's murder. While she becomes a defendant and
                     Ji Wook who is known as a harsh prosecutor""",
                     genre = " Romance, comedy, legal, crime",
                     running_time="30 minutes",
                     no_of_episodes="40 (two episodes back-to-back)",
                     dramas=drama1)
session.add(dramalang8)
session.commit()

dramalang9=DramaLang(name="While You Were Sleeping",
                     description="""A supernatural romance about a woman who can see the future in her dreams and a prosecutor who fights to stop
                     these future events from happening.""",
                     genre = " Fantasy, legal, romance",
                     running_time="30 minutes",
                     no_of_episodes="32 (two episodes back-to-back)",
                     dramas=drama1)
session.add(dramalang9)
session.commit()

dramalang10=DramaLang(name="Healer",
                     description="""A mysterious messenger, an online newspaper reporter who only concerns her own interests, a popular reporter who
                     agonizes over the truth and reality.When these three people meet, a passionate romance starts and the truths from the past and present
                     reveal themselves to the world. This drama features young people and how they grow into real reporters.""",
                     genre = " Romance, comedy, thriller, action",
                     running_time="60 minutes",
                     no_of_episodes="20",
                     dramas=drama1)
session.add(dramalang10)
session.commit()
                     


drama2=Dramas(user_id=1,name=" Chinese Dramas")
session.add(drama2)
session.commit()

dramalang1=DramaLang(name="Love O2O",
                     description="""Story of two popular college students who fell in love through an online RPG game.""",
                     genre="Romance",
                     running_time="45 minutes",
                     no_of_episodes="30",
                     dramas=drama2)
session.add(dramalang1)
session.commit()

dramalang2=DramaLang(name="The Whirlwind Girl",
                     description="""A girl's pursuit for martial art glory and the friends she made along the way.""",
                     genre="  Martial arts, romance",
                     running_time="30-35 minutes",
                     no_of_episodes="32",
                     dramas=drama2)
session.add(dramalang2)
session.commit()

dramalang3=DramaLang(name="Boss and Me",
                     description="""Based off Gu Man's very popular internet novel, the story tells of a kind hearted young girl named
                     Xue Shan Shan (Zhao Li Ying) who works at a big conglomerate. However one of her weaknesses is eating, she loves to eat,
                     and so upon discovering this her boss, Feng Teng (Zhang Han) decides to intentionally fatten her up; she
                     just so happens to share the same blood type as his sister, and thus has the motive of making her the blood donor.
                     Hence comedy ensues as she melts his heart with her exceptional appetite and her cute charm.""",
                     genre=" Romance, Modern Drama",
                     running_time="45 minutess",
                     no_of_episodes="34",
                     dramas=drama2)
session.add(dramalang3)
session.commit()

dramalang4=DramaLang(name="A Love So Beautiful",
                     description="""The ups and downs of school, family and growing up test the affection between a budding
                     artist and her handsome but indifferent classmate and neighbour.""",
                     genre=" Youth, romance",
                     running_time="20 minutes",
                     no_of_episodes="23",
                     dramas=drama2)
session.add(dramalang4)
session.commit()

dramalang5=DramaLang(name="Best Time",
                     description="""In high school, Su Man (Janine Chang) fell in love with Song Yi (Jia Nailiang), a student with good academics
                     and superior basketball skills. She was then admitted to Tsinghua University School of Management and have never heard about
                     him since. Ten years later, Su Man finds out that Song Yi is back from the United States and is the new director of MG Company.
                     She decides to join the company and applies for a clerk post faking her resume. The Chief Investment Officer Lu Licheng (Wallace Chung)
                     , who aspires to become the CEO of the company, finds out her true identity and threatens her; yet he appreciates her talent and
                     keeps her by his side. The events took an unexpected turn when Su Man's best friend falls for Song Yi, and Lu Licheng develops
                     feelings for Su Man.""",
                     genre=" Melodrama, romance",
                     running_time="25 minutes",
                     no_of_episodes="47",
                     dramas=drama2)
session.add(dramalang5)
session.commit()

dramalang6=DramaLang(name="Love Me, If You Dare",
                     description="""Simon is a criminal profiler from the US who retreats to China in the aftermath of an intense encounter with a
                     serial killer. He hires Jenny to help him with his work, and they fall in love. But a serial-killer stalker is leaving calling
                     cards for Simon in other killers' crime scenes. The suspect pool is small. Someone who knows Simon's terrible ordeal. Someone
                     who sees Simon as a friend. Someone who is willing to kill Jenny to get to Simon.""",
                     genre=" Romance, crime, thriller",
                     running_time="43 minutes",
                     no_of_episodes="24",
                     dramas=drama2)
session.add(dramalang6)
session.commit()

dramalang7=DramaLang(name="Memory Lost",
                     description="""A woman lost her identity and her memory after getting kidnapped by a criminal organization. Her boyfriend was
                     injured in the same incident and forgot her face, yet he never stopped looking for her. Many years later, a string of criminal activities
                     reunited them. Although they were now strangers, their complementary skill sets made them formidable partners within a police
                     task force called Black Shield. As they grew closer, her past came back to haunt them.""",
                     genre="Crime, police, romance",
                     running_time="43 minutes",
                     no_of_episodes=" 3 seasons, 12 episodes each season",
                     dramas=drama2)
session.add(dramalang7)
session.commit()

dramalang8=DramaLang(name="Rush to the Dead Summer",
                     description="""Despite growing up poor, Li Xia works hard and wins a scholarship into a grand secondary school where she meets
                     the legendary Fu Xiaosi and Lu Zhi'ang. Love booms in more ways than one, and the group of youth quickly became good friends. After
                     graduation, everyone goes their separate ways. Xiaosi becomes a well-known artist, Li Xia becomes Xiaosi's assistant and other half,
                     Qiqi won a singing competition and becomes a famous idol, Yu Jian heads overseas to realize her dreams of becoming a singer.
                     However, with the onslaught of adversities: the death of Xiaosi's mother, Li Xia's departure, imprisonment of Zhi'ang, Qiqi's betrayal,
                     Yu Jian's loss; the warm and bright summer starts to fade away. Everyone is changing and they become doubtful about the origin of their
                     friendship. A span of ten years make them realize that other than memories, nothing can be eternal, but at least they learnt
                     to love and grow.""",
                     genre="Youth, romance",
                     running_time="20 minutes",
                     no_of_episodes=" 48",
                     dramas=drama2)
session.add(dramalang8)
session.commit()

dramalang9=DramaLang(name="My Story For You",
                     description="""It's 1998, and Zhang Changgong gets his first taste of success as a developer in an IT company. At the
                     same time, he meets and falls in love with Li Muzi (Zheng Shuang), a kind and intelligent university student. Unfortunately
                     the IT bubble soon bursts, and Zhang Changgong is left unemployed. With the help of his friends and family, Changgong faces
                     the challenges head on, and eventually becomes a top-selling author.""",
                     genre="metropolitan, romance, coming-of-age",
                     running_time="45 minutes",
                     no_of_episodes="45",
                     dramas=drama2)
session.add(dramalang9)
session.commit()

dramalang10=DramaLang(name="In Love Through Thousands of Years",
                     description="""Imperial scholar official, Gong Ming(Jing Bo Ran) accidently time-travels two thousand years into
                     the present where he meets actress Lin Xiang Xiang(Zheng Shuang). Their story is one of love, fate, and commitment.""",
                     genre="Romance,Historical,Time Travel",
                     running_time="45 minutes",
                     no_of_episodes="20",
                     dramas=drama2)
session.add(dramalang10)
session.commit()


drama3=Dramas(user_id=1,name="Turkish Dramas")
session.add(drama3)
session.commit()

dramalang1=DramaLang(name="Ask Laftan Anlamaz",
                     description="""Hayat is a country girl with strict parents. She is in a love hate relationship with her boss Murat.
                     Hayat is full of secrets that can ruin her career and relationship.""",
                     genre="Comedy, Romance ",
                     running_time="120 minutes approx",
                     no_of_episodes="31",
                     dramas=drama3)
session.add(dramalang1)
session.commit()

dramalang2=DramaLang(name="Kara Sevda",
                     description="""A young artist finds herself obligated to sacrifice her love story for hiding a family secret.""",
                     genre=" Drama, Romance ",
                     running_time="120 minutes approx",
                     no_of_episodes="74",
                     dramas=drama3)
session.add(dramalang2)
session.commit()

dramalang3=DramaLang(name="Forbidden Love ",
                     description="""Having lost his wife eleven years ago, Adnan devoted all his attention to his daughter Nihal and his son Bulent.
                     Adnan, who lives in one of the most prominent mansions along the Bosporus in Istanbul with a relative's son Behlul, and his
                     children's nanny, meets Bihter who is also a socialite couple's daughter she is very elegant and beautiful, everyone who meets her
                     get stunned and jealous of her, and he falls in love with her. While searching for peace, safety and happiness in Adnan's mansion,
                     Bihter meets passion. Behlul and Bihter fall completely into each other and become drowned by their infatuation with each other.
                     Their secret love affair will soon affect every member of the family.""",
                     genre="Drama, Romance ",
                     running_time="120 minutess approx",
                     no_of_episodes="79",
                     dramas=drama3)
session.add(dramalang3)
session.commit()

dramalang4=DramaLang(name="Medcezir ",
                     description="""Yaman,who lives in one of the Istanbul's suburbs,is arrested and put in jail along with his brother Kenan for
                     his brother stole a car at a gas station.Yaman gets a chance for a brand new start when he meets a lawyer Selim who takes Yaman
                     to his new home.""",
                     genre=" Comedy, Drama, Romance",
                     running_time="120 minutes approx",
                     no_of_episodes="77",
                     dramas=drama3)
session.add(dramalang4)
session.commit()

dramalang5=DramaLang(name="Heart Of The City",
                     description="""Heart of the City (Bu Sehir Arkandan Gelecek) is the story of Ali, a handsome sailor, brought up aboard a cargo
                     ship by Rauf, who saved him as a child after they were both witness to the murder of his mother at the hands of his father.Rauf
                     doesn't just take good care of Ali but also the ship's crew and he is affectionately referred to as their Mother.Raised
                     at sea, Ali is still terrified to return to his roots in Istanbul and the trauma of his mother's death, even after 20 years.
                     When one day he is forced off the ship he encounters the enchanting ballet dancer Derin, and immediately falls for her,
                     chasing her deep in to the city to save a potentially disastrous audition.""",
                     genre=" Drama",
                     running_time="120 minutes approx",
                     no_of_episodes="70",
                     dramas=drama3)
session.add(dramalang5)
session.commit()

dramalang6=DramaLang(name="Kara Para",
                     description="""Omar, a police officer loses his fiance to a suspicious death and he won't stop until he uncovers the truth.""",
                     genre="Action, Crime, Drama ",
                     running_time="120 minutes approx",
                     no_of_episodes="54",
                     dramas=drama3)
session.add(dramalang6)
session.commit()

dramalang7=DramaLang(name="Love and Punishment",
                     description="""After discovering her fiance's infidelity, Yasemin's journey of wild revenge destroys a promise.""",
                     genre="Action, Drama, Romance ",
                     running_time="120 minutes approx",
                     no_of_episodes="62",
                     dramas=drama3)
session.add(dramalang7)
session.commit()

dramalang8=DramaLang(name="Karadayi",
                     description="""The Kara family's life is turned upside down because of a wrongful accusation that results in the
                     imprisonment of Nazif Kara for a murder he didn't commit.""",
                     genre="Action, Crime, Drama ",
                     running_time="120 minutes approx",
                     no_of_episodes="105",
                     dramas=drama3)
session.add(dramalang8)
session.commit()

dramalang9=DramaLang(name="Sila",
                     description="""Taimoor and Mariam married each other against the wishes of their families in Southeastern Turkey
                     leads to tragedy and social change.. See the consequences of their marriage and how story unfolds.""",
                     genre="Drama, Mystery, Romance  ",
                     running_time="120 minutes approx",
                     no_of_episodes="79",
                     dramas=drama3)
session.add(dramalang9)
session.commit()

dramalang10=DramaLang(name="Son",
                     description="""After a plane crash, a woman finds out that her marriage was a lie.""",
                     genre="Adventure, Drama, Mystery   ",
                     running_time="120 minutes approx",
                     no_of_episodes="49",
                     dramas=drama3)
session.add(dramalang10)
session.commit()


drama4=Dramas(user_id=1,name="American Dramas")
session.add(drama4)
session.commit()

dramalang1=DramaLang(name="Game of Thrones ",
                     description="""Nine noble families fight for control over the mythical lands of Westeros, while an ancient
                     enemy returns after being dormant for thousands of years.""",
                     genre="Action, Adventure, Drama ",
                     running_time="57 minutes",
                     no_of_episodes="8 seasons, 73 episodes",
                     dramas=drama4)
session.add(dramalang1)
session.commit()

dramalang2=DramaLang(name="Grey's Anatomy",
                     description="""Surgical interns and their supervisors embark on a medical journey where they become part
                     of heart-wrenching stories and make life-changing decisions in order to become the finest doctors.""",
                     genre="Drama, Romance  ",
                     running_time="41 minutes",
                     no_of_episodes="14 seasons, 317 episodes",
                     dramas=drama4)
session.add(dramalang2)
session.commit()

dramalang3=DramaLang(name="Breaking Bad",
                     description="""Walter White, a chemistry teacher, discovers that he has cancer and decides to get into
                     the meth-making business to repay his medical debts. His priorities begin to change when he partners with Jesse.""",
                     genre="Crime, Drama, Thriller",
                     running_time="49 minutes",
                     no_of_episodes="5 seasons, 62 episodes",
                     dramas=drama4)
session.add(dramalang3)
session.commit()

dramalang4=DramaLang(name="Orange Is the New Black",
                     description="""Ten years after transporting drug money to Alex, Piper is imprisoned for the crime.
                     The toughness of prison changes her drastically as an individual, compelling her to do the unthinkable.""",
                     genre="Crime, Drama, Crime",
                     running_time="49 minutes",
                     no_of_episodes="5 seasons, 81 episodes",
                     dramas=drama4)
session.add(dramalang4)
session.commit()

dramalang5=DramaLang(name="Friends",
                     description="""Take a look at some of the best episodes of 'Friends', the story of six friends
                     living in Manhattan, who experience comfort and companionship with each other as they indulge in many adventures.""",
                     genre="Comedy, Romance",
                     running_time="22 minutes",
                     no_of_episodes="10 seasons, 236 episodes",
                     dramas=drama4)
session.add(dramalang5)
session.commit()

dramalang6=DramaLang(name="Will & Grace",
                     description="""Will, a gay lawyer, allows his best friend Grace, an interior designer, to stay in his house for
                     a temporary period after her marriage falls apart. But she ends up being his permanent roommate.""",
                     genre="Comedy, Romance",
                     running_time="22 minutes",
                     no_of_episodes="9 seasons, 210 episodes",
                     dramas=drama4)
session.add(dramalang6)
session.commit()

dramalang7=DramaLang(name="13 Reasons Why ",
                     description="""Follows teenager Clay Jensen, in his quest to uncover the story behind his classmate and crush, Hannah,
                     and her decision to end her life.""",
                     genre="Drama, Mystery",
                     running_time="60 minutes",
                     no_of_episodes="2 seasons, 39 episodes",
                     dramas=drama4)
session.add(dramalang7)

dramalang8=DramaLang(name="The Royals",
                     description="""The royal family is thrown into turmoil when the heir to the throne dies suddenly.
                     His younger siblings have a hard time with their new roles, while the queen tries to secure her grasp on the throne.""",
                     genre="Drama",
                     running_time="42 minutes",
                     no_of_episodes="4 seasons, 40 episodes",
                     dramas=drama4)
session.add(dramalang8)
session.commit()

dramalang9=DramaLang(name="2 Broke Girls",
                     description="""Max and Caroline, two girls in their mid-twenties, work at a Brooklyn restaurant as waitresses.
                     Together, they dream of starting up their cupcake business, but always find themselves without money.""",
                     genre="Comedy",
                     running_time="22 minutes",
                     no_of_episodes="6 seasons, 138 episodes",
                     dramas=drama4)
session.add(dramalang9)
session.commit()

dramalang10=DramaLang(name="The Big Bang Theory",
                     description="""The lives of socially awkward physicists Leonard Hofstadter and Sheldon Cooper take a
                     wild turn when the beautiful and free-spirited Penny moves in next door.""",
                     genre="Comedy, Romance",
                     running_time="22 minutes",
                     no_of_episodes="12 seasons, 280 episodes",
                     dramas=drama4)
session.add(dramalang10)
session.commit()


drama5=Dramas(user_id=1,name="British Dramas")
session.add(drama5)
session.commit()

dramalang1=DramaLang(name="Downton Abbey",
                     description="""Robert Crawley risks losing the family estate after his heirs die during the sinking of the Titanic.
                     Soon, the Crawleys are introduced to Matthew, the next in line who resists the ways of aristocrats.""",
                     genre="Drama, Romance ",
                     running_time="52 minutes",
                     no_of_episodes="6 seasons, 52 episodes",
                     dramas=drama5)
session.add(dramalang1)
session.commit()

dramalang2=DramaLang(name="The Crown",
                     description="""Follows the political rivalries and romance of Queen Elizabeth II's reign and the events
                     that shaped the second half of the 20th century.""",
                     genre="Drama, History",
                     running_time="58 minutes",
                     no_of_episodes="2 seasons, 20 episodes",
                     dramas=drama5)
session.add(dramalang2)
session.commit()

dramalang3=DramaLang(name="The Queen",
                     description="""Her Majesty Queen Elizabeth II delivers her annual address in the Christmas message to the nation and Commonwealth.""",
                     genre="Drama, History",
                     running_time="46 minutes",
                     no_of_episodes="1 seasons, 5 episodes",
                     dramas=drama5)
session.add(dramalang3)
session.commit()

dramalang4=DramaLang(name="Unforgotten",
                     description="""Police start to investigate when the bones of a young man are found under the footings of a demolished house 39 years
                     after his murder.""",
                     genre="Crime, Drama, Mystery ",
                     running_time="45 minutes",
                     no_of_episodes="3 seasons, 18 episodes",
                     dramas=drama5)
session.add(dramalang4)
session.commit()

dramalang5=DramaLang(name="Waking the Dead",
                     description="""A specialised team of police officers uses newfound evidence and new technology to try and solve cold cases. Led by
                     the temperamental Detective Superintendent Peter Boyd, the experts work on bringing justice to murder victims and their families.""",
                     genre="Crime, Drama, Mystery ",
                     running_time="100 minutes",
                     no_of_episodes="9 seasons, 92 episodes",
                     dramas=drama5)
session.add(dramalang5)
session.commit()

dramalang6=DramaLang(name="Murder in Suburbia",
                     description="""Detective Inspector Kate "Ash" Ashurst and Detective Sergeant Emma "Scribbs" Scribbins make up the sexy, sassy,
                     crime-busting duo who solve murders in the sleepy suburban town of Middleford in this U.K. crime drama.""",
                     genre="Crime, Drama, Mystery ",
                     running_time="60 minutes",
                     no_of_episodes="2 seasons, 12 episodes",
                     dramas=drama5)
session.add(dramalang6)
session.commit()

dramalang7=DramaLang(name="The Syndicate",
                     description="""The story revolves around five workers in a supermarket in Leeds whose lives table turn around when they jointly win the lottery.""",
                     genre="Drama",
                     running_time="60 minutes",
                     no_of_episodes="3 seasons, 17 episodes",
                     dramas=drama5)
session.add(dramalang7)
session.commit()

dramalang8=DramaLang(name="Bluestone 42",
                     description="""Examine the life of a bomb disposal detachment in Afghanistan.""",
                     genre="Comedy, War",
                     running_time="30 minutes",
                     no_of_episodes="3 seasons, 21 episodes",
                     dramas=drama5)
session.add(dramalang8)
session.commit()

dramalang9=DramaLang(name="A Passionate Woman",
                     description="""Leeds, 1950s, Betty is a married mother whose life is changed forever after falling hopelessly in love with her
                     charismatic neighbour.""",
                     genre="Drama",
                     running_time="90 minutes",
                     no_of_episodes="1 seasons, 2 episodes",
                     dramas=drama5)
session.add(dramalang9)
session.commit()

dramalang10=DramaLang(name="Prisoners' Wives",
                     description="""Following women struggling with the fall-out from the imprisonment of their loved ones.""",
                     genre="Drama",
                     running_time="60 minutes",
                     no_of_episodes="2 seasons, 10 episodes",
                     dramas=drama5)
session.add(dramalang10)
session.commit()


latestDrama1=LatestDramas(name="Latest Dramas")
session.add(latestDrama1)
session.commit()

latestDramaLang1=LatestDramaLang(name="Stranger Things",
                     description="""This thrilling Netflix original drama stars Golden Globe-winning actress Winona Ryder as Joyce Byers, 
                                who lives in a small Indiana town in 1983 -- inspired by a time when tales of science fiction captivated audiences. 
                                When Joyce's 12-year-old son, Will, goes missing, she launches a terrifying investigation into his disappearance with
                                local authorities. As they search for answers, they unravel a series of extraordinary mysteries involving secret 
                                government experiments, unnerving supernatural forces, and a very unusual little girl.""",
                     genre = "Science Fiction, Horror fiction, Supernatural fiction, Historical period drama",
                     running_time="42-62 minutes",
                     no_of_episodes="17",
                     latestDramas=latestDrama1)
session.add(latestDramaLang1)
session.commit()

latestDramaLang2=LatestDramaLang(name="What's Wrong with Secretary Kim",
                     description="""Revolves around the narcissistic Vice President of a major corporation, Lee Young-Joon, and his highly capable secretary. 
                                    Misunderstandings arise when she announces that she will resign from her position, after working for Lee Young-Joon for
                                    nine years.""",
                     genre = "Romance comedy",
                     running_time="90 minutes",
                     no_of_episodes="16",
                     latestDramas=latestDrama1)
session.add(latestDramaLang2)
session.commit()

latestDramaLang3=LatestDramaLang(name="Something in the Rain",
                     description="""When a single career woman reunites with her best friend's younger brother after he returns from three years of working
                                    abroad, their efforts to reconnect grow into romance.""",
                     genre = "Romance",
                     running_time="60 minutes",
                     no_of_episodes="16",
                     latestDramas=latestDrama1)
session.add(latestDramaLang3)
session.commit()

latestDramaLang4=LatestDramaLang(name="Radio Romance ",
                     description="""Song Geu Rim (Kim So Hyun) works as a radio program writer. Her mother is blind, and as a child she 
                                   listened to the radio frequently with her mother. This led her to become a radio program writer, but she isn't 
                                   exactly talented in writing. Now, the radio program that she works on is facing cancellation.
                                    Song Geu Rim succeeds in casting top actor Ji Soo Ho (Yoon Doo Joon) to try to save the show """,
                     genre = "Romance, Film",
                     running_time="60 minutes",
                     no_of_episodes="16",
                     latestDramas=latestDrama1)
session.add(latestDramaLang4)
session.commit()


latestDramaLang5=LatestDramaLang(name="I'm Not a Robot",
                     description="""The story of a man who lives an isolated life due to a severe allergy to other people but meets
                                    and falls in love with a woman who pretends to be a robot.""",
                     genre = "Romance Comedy",
                     running_time="35 minutes",
                     no_of_episodes="32",
                     latestDramas=latestDrama1)
session.add(latestDramaLang5)
session.commit()

latestDramaLang6=LatestDramaLang(name="Are You Human?",
                     description="""The drama tells of an android called Nam Shin III who must pretend to be the son of a rich family
                                    when the real Nam Shin falls into a coma. Nam Shin's mother, Oh Ro Ra is a genius on brain technology
                                    and artificial intelligence (AI) so when her son, the real Nam Shin, is taken away from her at a young age,
                                    in her grief she creates an android that looksexactly like her son and has it grow up in the place of Nam Shin. 
                                    But when Nam Shin, who is a third generation heir to PK group, gets in an accident and is comatose, 
                                    the android Nam Shin III must learn how to take his place. """,
                     genre = "Science Fiction, Romance Film, Political fiction, Mystery",
                     running_time="35 minutes",
                     no_of_episodes="36",
                     latestDramas=latestDrama1)
session.add(latestDramaLang6)
session.commit()
print ("added Dramas!")
