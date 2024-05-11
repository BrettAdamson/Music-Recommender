from flask import Blueprint
import os
from dotenv import load_dotenv
import requests


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/getdata")
def getdata():
    return {"key": "value"}


@api.route("/spotify_token", methods=["GET"])
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
