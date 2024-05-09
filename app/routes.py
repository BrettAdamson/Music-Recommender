from app import app
import requests
from flask import render_template, flash
from app.forms import SongForm
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


@app.route("/")
@app.route("/index")
def index():
    access_token()
    print("exited function")
    user = {"username": "Brett"}

    return render_template("index.html", title="Home", user=user)


@app.route("/search", methods=["GET", "POST"])
def song_search():
    form = SongForm()
    if form.validate_on_submit():
        print("valid")
        flash("{} by {}".format(form.song.data, form.artist.data))
        # return redirect("/index")
    else:
        print("invalid song")

    return render_template("song_form.html", title="Song Search", form=form)


@app.route("/spotify_token")
def access_token():
    print("in access token")
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    res = requests.post("https://accounts.spotify.com/api/token", data=payload)
    print(res.text)
    return res.text
