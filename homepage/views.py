from flask import render_template, request, flash

from .models import IpInfo
from .forms import SendEmailForm
from .mailing import compose_message
from . import app, db, mail, basic_auth
from .security import captcha_verified, track


@app.route('/', methods=['GET', 'POST'])
@track
def index():
    if request.method == 'GET':
        return render_template('index.html', form=SendEmailForm())

    form = SendEmailForm(request.form)
    verified = captcha_verified()

    if not verified:
        flash('Prosím potvrďte, že nejste robot.', 'alert-danger')

    if verified and form.validate():
        mail.send(compose_message())
        flash('Mail odeslán', 'alert-success')
        form = SendEmailForm()

    return render_template('index.html', form=form, anchor='kontakt')


@app.route('/submit_successful')
def submit_successful():
    flash('Mail odeslán', 'alert-success')
    return render_template('index.html', form=SendEmailForm())


@app.route('/traffic')
@basic_auth.required
def traffic():
    results = db.session \
        .query(IpInfo.city, db.func.count(IpInfo.id).label('count')) \
        .group_by(IpInfo.city) \
        .order_by('count desc') \
        .all()

    return render_template('traffic.html', results=results)
