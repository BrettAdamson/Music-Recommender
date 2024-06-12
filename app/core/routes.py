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
    return render_template("index.html", title="Home")


@bp.route("/search", methods=["GET", "POST"])
def song_search_form():
    form = SongForm()
    if form.validate_on_submit():
        spotify_data = song_search(form.artist.data, form.song.data)
        return render_template(
            "song_form.html",
            title="Song Search",
            form=form,
            song_name=spotify_data["song_name"],
            artist_name=spotify_data["artist_name"],
            album_image=spotify_data["album_image"],
            recommendation_tracks=spotify_data["recommendation_tracks"],
            preview_url=spotify_data["preview_url"],
        )
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)


def song_search(input_artist, input_song):
    if input_artist and input_song:
        track = spotify_handler.search_song(input_artist, input_song)
        album_name = track["album"]["name"]
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]
        album_image = track["album"]["images"][0]["url"]
        track_id = track["id"]
        preview_url = track["preview_url"]
        recommendations = spotify_handler.recommend_song_by_track(track_id)
        recommendation_tracks = recommendations["tracks"]
        # return track
        spotify_data = {
            "song_name": song_name,
            "artist_name": artist_name,
            "album_image": album_image,
            "recommendation_tracks": recommendation_tracks,
            "preview_url": preview_url,
        }
        return spotify_data
    else:
        print("invalid song")

    return "Invalid Inputs"
