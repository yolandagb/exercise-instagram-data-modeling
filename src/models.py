import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Post(Base):
     __tablename__ = 'post'
     id = Column(Integer, primary_key=True)
    user_name = Column(String(250))

class User(Base):
     __tablename__ = 'user'
     id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email= Column(String(250))

class Follower(Base):
     __tablename__ = 'follower'
     id = Column(Integer, primary_key=True)
    user_from_id = Column(String(250))  
    user_to_id =  Column(String(250))  

class User(Base):
     __tablename__ = 'user'
     id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email= Column(String(250))    

class Media(Base):
     __tablename__ = 'media'
     id = Column(Integer, primary_key=True)
     type = Column(String(250))
     url = Column(String(250))
     post_id = Column(String(250))
    

class Comment(Base):
     __tablename__ = 'commet'
     id = Column(Integer, primary_key=True)
     comment_text = Column(String(250))
     author_id= Column(String(250))
     post_id = Column(String(250))
        

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')