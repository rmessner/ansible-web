from flask import jsonify, request
from webapp import app, db
import flask
from webapp.model.history import History
from webapp.model.playbook import Playbook
from webapp.model.user import User
from webapp.tasks import playbook
from webapp.jsonp_helper import support_jsonp

__author__ = 'ramessne'

@app.route('/playbooks')
@support_jsonp
def list_playbooks():
    playbooks = Playbook.query.order_by(Playbook.name).all()
    result = []
    for item in playbooks:
        result.append(item.getDict())
    return jsonify(playbooks=result)

@app.route('/playbooks/<name>')
@support_jsonp
def detail_playbook(name=None):
    result = Playbook.query.filter_by(name=name).first()
    return jsonify(playbook=result.getDict())

@app.route('/playbooks/<name>/history')
@support_jsonp
def history_playbook(name=None):
    playbook = Playbook.query.filter_by(name=name).first()
    result = []
    for item in playbook.executions:
      result.append(item.getDict())
    return jsonify(histories=result)

@app.route('/playbooks/<name>/update')
@support_jsonp
def update_playbook(name=None):
    flask.abort(404)
    return ""

@app.route('/playbooks/<name>/delete')
@support_jsonp
def delete_playbook(name=None):
    flask.abort(404)
    return ""

@app.route('/playbooks/<name>/run')
@support_jsonp
def run_playbook(name=None):
    play = Playbook.query.filter_by(name=name).first()
    #user = User.query.filter_by(api_key=request.form["api_key"]).first()
    #if ( play == None or user == None):
    #    flask.abort(404)

    item = History()
    #	item.user = user
    item.playbook = play
    item.status = "pending"

    db.session.add(item)
    db.session.commit()
    
    item.log_path = "playbooks_dir/%s/logs/%s.log" % (play.id, item.id)

    db.session.commit()

    playbook.run.delay(item.id)

    return jsonify(run=item.getDict())
