from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ListForm(FlaskForm):
    name = StringField("List name", [validators.Length(min=1)])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=1)])

    class Meta:
        csrf = False

