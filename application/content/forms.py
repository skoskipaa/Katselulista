from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class ContentForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=1, max=100)])
    length = IntegerField("Length (in minutes)", [validators.NumberRange(min=0, max=999999)])
    category = SelectField("Category", choices=[("Drama", "Drama"), ("Comedy", "Comedy"), ("Scifi", "Scifi"),
    ("Horror", "Horror"), ("Action", "Action"), ("Romance", "Romance"), ("Kids", "Kids")])
    cdn = SelectField("Content provider", choices=[("HBO", "HBO"), ("Netflix", "Netflix"), ("Amazon Prime", "Amazon Prime")])

    class Meta:
        csrf = False

class EditContentForm(FlaskForm):
   
    name = StringField("Title", [validators.Length(min=1, max=100)])
    length = IntegerField("Length (in minutes)", [validators.NumberRange(min=0, max=999999)])
    category = SelectField("Category", choices=[("Drama", "Drama"), ("Comedy", "Comedy"), ("Scifi", "Scifi"),
    ("Horror", "Horror"), ("Action", "Action"), ("Romance", "Romance"), ("Kids", "Kids")])
    cdn = SelectField("Content provider", choices=[("HBO", "HBO"), ("Netflix", "Netflix"), ("Amazon Prime", "Amazon Prime")])

    class Meta:
        csrf = False