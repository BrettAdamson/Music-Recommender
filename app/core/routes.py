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
        album_name = track["album"]["name"]
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]
        album_image = track["album"]["images"][0]["url"]
        print(track["album"]["name"])
        print(track["artists"][0]["name"])
        print(track["name"])
        print(track["album"]["images"][0]["url"])
        return render_template(
            "song_form.html",
            title="Song Search",
            form=form,
            song_name=song_name,
            artist_name=artist_name,
            album_image=album_image,
        )
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)
