import logging
from functools import wraps
from datetime import datetime

import requests
from flask import request

from . import app, db
from .models import IpInfo

GOOGLE_CAPTCHA_VERIFICATION_URL = 'https://www.google.com/recaptcha/api/siteverify'
GEOLOCATION_API_URL = 'http://ip-api.com/json/{}'


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


def track(view):
    @wraps(view)
    def log_ip(*args, **kwargs):
        """ Loads request's IP, gets GEO data and stores it in DB. """

        url = GEOLOCATION_API_URL.format(request.remote_addr)
        response = requests.get(url).json()

        if response['status'] == 'success':
            ip_info = IpInfo(country=response['country'],
                             city=response['city'],
                             zip=response['zip'],
                             lat=float(response['lat']),
                             lon=response['lon'],
                             timezone=response['timezone'],
                             datetime=datetime.now())
        else:
            logging.warning('Failed to get IP info.')
            ip_info = IpInfo(datetime=datetime.now())

        db.session().add(ip_info)
        db.session().commit()

        return view(*args, **kwargs)

    return log_ip
