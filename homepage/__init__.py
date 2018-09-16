from flask import Flask
from flask_mail import Mail
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

__all__ = ('app', 'db', 'mail')

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('homepage.config')

mail = Mail(app)

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

# Importing at the end of file is ugly, but necessary
# http://flask.pocoo.org/docs/0.12/patterns/packages/
import homepage.views
import homepage.models
