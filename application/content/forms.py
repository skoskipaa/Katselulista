from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class ContentForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=1)])
    length = IntegerField("Length (in minutes)")
    category = SelectField("Category", choices=[("Drama", "Drama"), ("Comedy", "Comedy"), ("Scifi", "Scifi"),
    ("Horror", "Horror"), ("Action", "Action"), ("Romance", "Romance"), ("Kids", "Kids")])
    cdn = SelectField("Content provider", choices=[("HBO", "HBO"), ("Netflix", "Netflix"), ("Amazon Prime", "Amazon Prime")])

    class Meta:
        csrf = False

