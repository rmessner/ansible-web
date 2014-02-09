import json
from flask import render_template, jsonify
from flask.globals import request
from webapp import app
from webapp.model.user import User
from webapp.tasks import playbook

__author__ = 'ramessne'

@app.route('/')
def index(name=None):
    playbook.run.delay(23, 42)
    return render_template('index.html')

@app.route('/login')
def login():
    result = None
    email = request.args["email"]
    password = request.args["pwd"]
    user = User.query.filter_by(email=email.lower()).first()
    if ( user != None and user.checkPassword(password) ):
        result = user.getDict()
    return jsonify(user=result)