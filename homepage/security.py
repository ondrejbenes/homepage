import requests
from flask import request

from . import app

GOOGLE_CAPTCHA_VERIFICATION_URL = 'https://www.google.com/recaptcha/api/siteverify'


def verify_captcha():
    params = {
        'secret': app.config['RECAPTCHA_KEY'],
        'response': request.form['g-recaptcha-response'],
        'remoteip': request.remote_addr
    }
    resp = requests.post(GOOGLE_CAPTCHA_VERIFICATION_URL, data=params)
    resp.raise_for_status()

    if not resp.json()['success']:
        raise ValueError('Captcha validation unsuccessful')

# TODO Tracking
