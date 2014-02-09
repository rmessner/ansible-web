from idlelib.macosxSupport import hideTkConsole

__author__ = 'ramessne'

from webapp import db
db.drop_all()
db.create_all()

from webapp.model.user import User
from webapp.model.playbook import Playbook
from webapp.model.history import History

guest = User('guest','guest@sample.com')
guest2 = User('admin','admin2')
playbook = Playbook('test')
history = History()
history.playbook = playbook
history.user = guest
history2 = History()
history2.playbook = playbook
history2.user = guest
db.session.add(guest)
db.session.add(guest2)
db.session.add(playbook)
db.session.add(history)
db.session.add(history2)
db.session.commit()

tmp = playbook.executions

for assoc in tmp:
    print assoc.id
    print assoc.user.email
