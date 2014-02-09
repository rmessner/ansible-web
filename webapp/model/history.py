from webapp import db

__author__ = 'ramessne'

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_path = db.Column(db.String(255), unique=True)
    status = db.Column(db.Enum('pending','running','failed','succeeded', name='history_status_type'))

    playbook_id = db.Column(db.Integer, db.ForeignKey('playbook.id'))
    playbook = db.relationship('Playbook', backref=db.backref('executions', lazy='joined'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('executions', lazy='joined'))

    def getDict(self):
        return dict(id=str(self.id), status=str(self.status), playbook_id=str(self.playbook_id), user_id=str(self.user_id))