import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True, nullable = False)
    firstname = Column(String(250),unique = True, nullable = False)
    lastname = Column(String(250), unique = True, nullable = False)
    email = Column(String(250), unique = True, nullable = False)
    favorite_Post = relationship('Post', backref = 'User', uselist = False)
    favorite_Likes = relationship('Likes', backref = 'User', uselist = False)

class Comment_text(Base):
    __tablename__ = 'Comment_text'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable = False)
    author_id = Column(Integer, ForeignKey(User.id))
    post_id = Column(Integer, nullable = True)

class Post(Base):
    __tablename__ ='Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey(User.id),nullable = False)

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    User_from_id = Column(Integer,ForeignKey(User.id), nullable = False)
    User_to_id = Column(Integer, nullable = False)

class Likes(Base):
    __tablename__ ='Likes'
    id = Column(Integer, primary_key = True)
    Likes_to_followers = Column(Integer,ForeignKey(User.id), nullable = False)
    Likes_to_User = Column(Integer, nullable = False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
