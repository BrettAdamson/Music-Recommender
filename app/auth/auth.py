import os
from dotenv import load_dotenv
import requests
from app.api import bp
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import redirect, request, session, g, request, redirect, url_for
import json
from functools import wraps

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
    access_token = response.json()["access_token"]
    session["auth_code"] = access_token
    return json.dumps(response.json())


@bp.route("/client_credentials", methods=["GET"])
def access_token():
    print("in access token")
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload)
    print(response.text)
    access_token = response.json()["access_token"]
    session["client_code"] = access_token
    if session["client_code"]:
        print("CREDENTIALS: \n")
        print(session["client_code"])
        print("\n")

    return json.dumps(response.json())


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            print("Authorization exists")
        else:
            print("Authorization does not exist")

        # x = 10
        # if x > 5:
        #     print("Token exists")
        # else:
        #     print("Token does not exist")
        return f(*args, **kwargs)

    return decorated_function
