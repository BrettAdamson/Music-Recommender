import os
from dotenv import load_dotenv
import requests
from app.api import bp
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import redirect, request
import json

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

REDIRECT_URI = "http://127.0.0.1:5000/redirect"
SCOPE = ["user-read-email", "playlist-read-collaborative"]
BASE_AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"


@bp.route("/oauth2_token")
def oauth_token():
    spotify = OAuth2Session(CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
    auth_url, state = spotify.authorization_url(BASE_AUTH_URL)
    print("url: " + auth_url)
    print("state: " + state)
    return redirect(auth_url)


@bp.route("/redirect")
def spotify_redirect():
    code = request.args.get("code")
    response = requests.post(
        TOKEN_URL,
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
    )
    return json.dumps(response.json())


@bp.route("/spotify_token", methods=["GET"])
def access_token():
    print("in access token")
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    res = requests.post("https://accounts.spotify.com/api/token", data=payload)
    print(res.text)
    return res.text
