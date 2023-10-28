import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorite = relationship('Favorite', uselist=True, backref='users')


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    gender = Column(String(20), nullable=True)
    hair_color = Column(String(30), nullable=True)
    eye_color = Column(String(30), nullable=True)
    favorite = relationship('Favorite', uselist=True, backref='characters')
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    terrain = Column(String(30), nullable=True)
    climate = Column(String(30), nullable=True)
    population = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=True )
    favorite = relationship('Favorite', uselist=True, backref='planets')




# # one to one
# class Parent(Base):
#     __tablename__='parents'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(80), nullable=False)
#     child = relationship('Child',  uselist=False)

# class Child(Base):
#     __tablename__='children'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(80), nullable=False)
#     parent_id = Column(Integer(), ForeignKey('parents.id'))

# # one to many
# class User(Base):
#     __tablename__='user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(40), nullable=False, unique=True)
#     email = Column(String(80), nullable=False, unique=True)
#     posts = relationship('Post', uselist=True, backref='user')

# class Post(Base):
#     __tablename__='posts'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), nullable=False)
#     content = Column(Text, nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))

# # many to many
# class Customer(Base):
#     __tablename__='customer'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     product_customer = relationship('Product_Customer', uselist=True, backref='customer')

# class Product(Base):
#     __tablename__='product'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     product_customer = relationship('Product_Customer', uselist=True, backref='product')

# class Product_Customer(Base):
#     __tablename__='product_customer'
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey('customer.id'))
#     product_id = Column(Integer, ForeignKey('product.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
