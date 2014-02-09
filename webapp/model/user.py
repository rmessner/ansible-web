import hashlib
from flask import json

__author__ = 'ramessne'

from webapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.Text, unique=True)
    api_key = db.Column(db.Text, unique=True)

    def __init__(self, p_email, p_password):
        self.email =p_email
        self.password = hashlib.sha512(p_email + p_password).hexdigest()
        self.api_key = hashlib.sha512(self.email + self.password).hexdigest()

    def getDict(self):
        return dict( id=str(self.id), email=str(self.email), api_key=str(self.api_key))

    def checkPassword(self, pwd):
        return self.password == hashlib.sha512(self.email + pwd).hexdigest()