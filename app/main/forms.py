"""表单"""

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    """name表单"""
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
