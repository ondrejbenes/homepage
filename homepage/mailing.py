from sendgrid.helpers.mail import Mail, Email, Content

from . import sendgrid_client, app


def send_email(sender_name, sender_email, message):
    """Sends an email using the Sendgrid API. Returns the API response."""

    subject = 'Zpráva z webu'
    content = Content('text/plain', f'{sender_name} napsal:\n{message}')
    mail = Mail(from_email=Email(sender_email),
                subject=subject,
                to_email=Email(app.config['MAIL_RECIPIENT']),
                content=content)
    return sendgrid_client.client.mail.send.post(request_body=mail.get())
