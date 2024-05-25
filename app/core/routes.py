from flask import render_template, flash, session
from app.forms import SongForm
from app.core import bp
from app.api import spotify_handler
from app.auth import auth
import requests
import json


@bp.route("/")
def index():
    print("exited function")
    user = {"username": "Brett"}
    return render_template("index.html", title="Home", user=user)


@bp.route("/search", methods=["GET", "POST"])
def song_search():
    form = SongForm()
    if form.validate_on_submit():
        print("valid")
        flash("{} by {}".format(form.song.data, form.artist.data))
        track = spotify_handler.search_song(form.artist.data, form.song.data)
        return track
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)
