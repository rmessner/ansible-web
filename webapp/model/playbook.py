from webapp import db

__author__ = 'ramessne'

class Playbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def getDict(self):
        return dict(id=str(self.id), name=str(self.name))
