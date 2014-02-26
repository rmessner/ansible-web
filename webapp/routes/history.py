from flask import jsonify, request
import flask
from webapp import app, db
from webapp.model.history import History
from webapp.model.playbook import Playbook
from webapp.model.user import User
from webapp.tasks import playbook
from webapp.jsonp_helper import support_jsonp

__author__ = 'ramessne'

@app.route('/history')
@support_jsonp
def list_history():
    histories = History.query.order_by(History.id).all()
    result = []
    for item in histories:
        result.append(item.getDict())
    return jsonify(histories=result)

@app.route('/history/<id>')
@support_jsonp
def detail_history(id=None):
    result = History.query.filter_by(id=id).first()
    if result == None:
       flask.abort(404)
    return jsonify(history=result.getDict())

@app.route('/history/<id>/log')
@support_jsonp
def log_history(id=None):
    item = History.query.filter_by(id=id).first()
    result = ""
    if item == None:
       flask.abort(404)
    with open(item.log_path, 'r') as output_f:
       result = output_f.read()
    return result
