from flask import request
from flask_mail import Message

from . import app


def compose_message():
    """Composes a message based on what was entered into the form."""
    msg = Message('Message from Homepage',
                  sender=app.config['MAIL_SENDER'],
                  recipients=app.config['MAIL_RECIPIENTS'])
    msg.body = '{name} ({email}) napsal:\n{message}'.format(**dict(request.form.items()))
    return msg
