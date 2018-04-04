from flask import Flask
from flask_mail import Mail

__all__ = ('app', 'mail')

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

app.config.from_envvar('APP_CONFIG_FILE')

mail = Mail(app)

# Importing at the end of file is ugly, but necessary
# http://flask.pocoo.org/docs/0.12/patterns/packages/
import homepage.views
