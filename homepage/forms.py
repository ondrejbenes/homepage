from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


# TODO Validators
class SendEmailForm(Form):
    email = StringField(u'Váš email', validators=[DataRequired(), Email()])
    name  = StringField(u'Vaše jméno', validators=[DataRequired()])
    message  = TextAreaField(u'Zpráva', validators=[DataRequired()])
