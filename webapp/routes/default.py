import json
from flask import render_template, jsonify, send_file
from flask.globals import request
from webapp import app
from webapp.model.user import User
from webapp.tasks import playbook

__author__ = 'ramessne'

@app.route('/')
def index(name=None):
    #return render_template('index.html')
    return send_file('templates/index.html')

@app.route('/login')
def login():
    result = None
    email = request.args["email"]
    print email
    password = request.args["pwd"]
    user = User.query.filter_by(email=email.lower()).first()
    if ( user != None and user.checkPassword(password) ):
        result = user.getDict()
    else:
        flask.abort(404)
    return jsonify(user=result)
