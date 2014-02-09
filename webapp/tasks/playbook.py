from webapp import celery, db
from webapp.model.history import History
import shlex, subprocess

__author__ = 'ramessne'

@celery.task
def demo(a, b):
    return a + b

@celery.task
def run( id ):
    item = History.query.filter_by(id=id).first()
    if item != None :
        item.status = "running"
        db.session.commit()
        command_line = "/usr/bin/ansible-playbook -i playbooks_dir/%s/playbook/hosts playbooks_dir/%s/playbook/site.yml -vvvv" % (item.playbook.id, item.playbook.id)
        print "##########" + command_line + "#############"
        #command_line = "/usr/bin/ansible-playbook"
        args = shlex.split(command_line)
        with open(item.log_path, 'w') as output_f:
            p = subprocess.call(args,
                        stdout=output_f,
                        stderr=output_f
                        )
        item.status = "succeeded"
    else:
        item.status = "failed"
    db.session.commit()