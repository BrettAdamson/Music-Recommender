from flask import render_template, flash, session
from app.forms import SongForm
from app.core import bp
from app.api import spotify_handler
from app.auth import auth
import requests
import json

# from app.api.routes import getdata


# @bp.before_request
# def check_tokens():
# print("checking tokens")
# if session["auth_code"]:
#     auth_token = session["auth_code"]
# elif session["client_code"]:
#     credential_token = session["client_code"]
# else:
#     auth.get_client_credentials()
# return

# if True:
#     authToken = auth.access_token()
#     print(authToken)


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
