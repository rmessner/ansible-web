from celery_init import make_celery
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify

__author__ = 'ramessne'

# Definition de l application
app = Flask("webapp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ramessne/ansible-playbooks/database.db'
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['SQLALCHEMY_ECHO'] = 'True'
# TODO ajouter a la config le chemin des playbooks
# TODO ajouter a la config le chemin des logs

# Connexion a la base de donnees
db = SQLAlchemy(app)
import model.history
import model.user
import model.playbook

# Connexion a celery pour les taches asynchrones
celery = make_celery(app)
# Import des taches asynchrones prise en charge
from tasks import playbook

# Import des routes de l application
import routes.default
import routes.playbooks
import routes.history


if __name__ == "__main__":
    app.run(debug=True,port=8080)
