from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SongForm(FlaskForm):
    song = StringField("Song", validators=[DataRequired()])
    artist = PasswordField("Artist", validators=[DataRequired()])
    submit = SubmitField("Submit")
