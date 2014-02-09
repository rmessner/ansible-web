from webapp.model.playbook import Playbook

__author__ = 'ramessne'

from webapp import db
db.drop_all()
db.create_all()

from webapp.model.user import User

admin = User("admin","admin")
db.session.add(admin)
db.session.commit()

play = Playbook("init")
db.session.add(play)
db.session.commit()
