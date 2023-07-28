import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')

    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")
    likes = relationship("Like", backref="user")

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('Person.id'), nullable=False)
    content = Column(Text, nullable=False)
    media_url = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')

    comments = relationship("Comment", backref="post")
    likes = relationship("Like", backref="post")

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('Person.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    comment_text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')

class Like(Base):
    __tablename__ = 'Like'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('Person.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
