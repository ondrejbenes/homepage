import os


DEBUG = os.getenv('DEBUG')

# Mailing
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
MAIL_RECIPIENT = os.getenv('MAIL_RECIPIENT')

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