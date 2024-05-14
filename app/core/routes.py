from flask import render_template, flash, Blueprint
from app.forms import SongForm
from app.core import bp
from app.api import spotify_handler

# from app.api.routes import getdata


@bp.route("/test")
def web_index():
    auth = spotify_handler.access_token()
    return auth


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
        # return redirect("/index")
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)
