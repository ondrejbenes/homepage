from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class SendEmailForm(Form):
    data_required_message = 'Pole musí být vyplněno'
    email_message = 'Nevalidní email'

    email = StringField(u'Váš email', validators=[DataRequired(message=data_required_message),
                                                  Email(message=email_message)])
    name  = StringField(u'Vaše jméno', validators=[DataRequired(message=data_required_message)])
    message  = TextAreaField(u'Zpráva', validators=[DataRequired(message=data_required_message)])
