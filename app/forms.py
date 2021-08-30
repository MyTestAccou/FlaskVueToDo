from wtforms import Form, StringField
from wtforms.validators import DataRequiered

class TaskForm(Form):
    title = StringField('title', validators=[DataRequiered()])