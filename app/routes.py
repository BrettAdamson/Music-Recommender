from app import app
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
