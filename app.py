from flask import Flask, render_template, request, redirect, url_for
from forms import SendEmailForm
from flask_mail import Mail, Message

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

app.config.from_envvar('APP_CONFIG_FILE')

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html', form=SendEmailForm())


# TODO Async
@app.route('/send-email', methods=['POST'])
def send_email():
    msg = Message('Message from Homepage',  # TODO Add Subject field
                  sender=app.config['MAIL_SENDER'],
                  recipients=app.config['MAIL_RECIPIENTS'])
    msg.body = '{name} ({email}) napsal:\n{message}'.format(**dict(request.form.items()))
    mail.send(msg)  # TODO prevent spamming (blacklist?)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
