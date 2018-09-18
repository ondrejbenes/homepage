import os


DEBUG = os.getenv('DEBUG')

# Mailing
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_SENDER = os.getenv('MAIL_USERNAME')
MAIL_RECIPIENTS = os.getenv('MAIL_RECIPIENTS','').split(',')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

# Google's Recaptcha
RECAPTCHA_KEY = os.getenv('RECAPTCHA_KEY')

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Basic Auth
BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')

# Flask session secret
SECRET_KEY = os.getenv('SECRET_KEY')