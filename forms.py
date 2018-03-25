from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


# TODO Validators
class SendEmailForm(Form):
    email = StringField(u'Email', validators=[DataRequired(), Email()])
    name  = StringField(u'Jméno', validators=[DataRequired()])
    message  = TextAreaField(u'Zpráva', validators=[DataRequired()])
