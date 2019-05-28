from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ListForm(FlaskForm):
    name = StringField("List name", [validators.Length(min=5)])

    class Meta:
        csrf = False

