from flask import render_template
from app.forms import SongForm
from app.core import bp
from app.api import spotify_handler


# @bp.route("/")
# def index():
#     print("exited function")
#     return render_template("index.html", title="Home")


@bp.route("/", methods=["GET", "POST"], defaults={"id": None})
@bp.route("/<id>", methods=["GET", "POST"])
def song_search_form(id):
    form = SongForm()
    if form.validate_on_submit():
        spotify_data = song_search(form.artist.data, form.song.data)
        return render_template(
            "song_form.html", title="Song Search", form=form, spotify_data=spotify_data
        )
    elif id is not None:
        spotify_data = song_search_by_id(id)
        return render_template(
            "song_form.html", title="Song Search", form=form, spotify_data=spotify_data
        )
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)


def song_search_by_id(id):
    if id is not None:
        track = spotify_handler.get_track(id)
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]
        album_image = track["album"]["images"][0]["url"]
        id = track["id"]
        preview_url = track["preview_url"]
        recommendations = spotify_handler.recommend_song_by_track(id)
        recommendation_tracks = recommendations["tracks"]
        spotify_url = track["external_urls"]["spotify"]
        spotify_data = {
            "song_name": song_name,
            "artist_name": artist_name,
            "album_image": album_image,
            "recommendation_tracks": recommendation_tracks,
            "preview_url": preview_url,
            "spotify_url": spotify_url,
        }
        return spotify_data
    else:
        print("invalid song")

    return "Invalid Inputs"


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
        spotify_url = track["external_urls"]["spotify"]
        # return track
        spotify_data = {
            "song_name": song_name,
            "artist_name": artist_name,
            "album_image": album_image,
            "recommendation_tracks": recommendation_tracks,
            "preview_url": preview_url,
            "spotify_url": spotify_url,
        }
        return spotify_data
    else:
        print("invalid song")

    return "Invalid Inputs"
