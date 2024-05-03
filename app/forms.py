from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SongForm(FlaskForm):
    song = StringField("Song", validators=[DataRequired()])
    artist = StringField("Artist", validators=[DataRequired()])
    submit = SubmitField("Submit")
