from flask import Blueprint
import os
from dotenv import load_dotenv
import requests
from app.api import bp


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# @bp.route("/getdata")
def getdata():
    return {"key": "value"}


@bp.route("/spotify_token", methods=["GET"])
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
