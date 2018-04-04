from flask import render_template, redirect, url_for

from . import app, mail
from .mailing import compose_message
from .security import verify_captcha
from .forms import SendEmailForm


@app.route('/')
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
