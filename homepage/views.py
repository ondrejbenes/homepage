from flask import render_template, redirect, url_for

from .models import IpInfo
from .forms import SendEmailForm
from .mailing import compose_message
from . import app, db, mail, basic_auth
from .security import verify_captcha, track


@app.route('/')
@track
def index():
    return render_template('index.html', form=SendEmailForm())


@app.route('/handle-email', methods=['POST'])
def handle_email():
    try:
        verify_captcha()
    except ValueError:
        pass  # TODO redirect with error

    mail.send(compose_message())

    return redirect(url_for('index'))


@app.route('/traffic')
@basic_auth.required
def traffic():
    results = db.session \
        .query(IpInfo.city, db.func.count(IpInfo.id).label('count')) \
        .group_by(IpInfo.city) \
        .order_by('count desc') \
        .all()

    return render_template('traffic.html', results=results)
