from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField


class PredictionForm(FlaskForm):

    image = FileField(validators=[FileRequired()])
    submit = SubmitField('Identify the sign')
