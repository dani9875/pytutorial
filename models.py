from enum import unique
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = tuple(db.UniqueContraint('id','username', name = 'myZuniq'))

    id = db.Column(db.String(), primary_key = True, unique=True)
    apiKey = db.Column(db.String(), primary_key = True, unique = True)
    username = db.Column(db.String(), primary_key = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    password = db.Column(db.String())
    emailadress = db.Column(db.String())

def __init__(self, id, username, first_name, last_name, password, emailadress):
    self.id = id
    self.username = username
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    self.emailadress = emailadress

def __repr__(self):
    return '<id {}'.format(self.id)

def serialize(self):
    return{
        'id': self.id,
        'username': self.username,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'password': self.password,
        'emailadress': self.emailadress
    }

