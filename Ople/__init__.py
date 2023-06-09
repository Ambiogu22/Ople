import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

login_manager = LoginManager()

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    db = SQLAlchemy(app)

with app.app_context():
    Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'
