import os
from dotenv import load_dotenv
import requests
from app.api import bp
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import redirect, request, session, request, redirect
import json
from functools import wraps
import urllib.error

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
    auth_token = response.json()
    session["auth_code"] = auth_token
    return response.json()


@bp.route("/client_credentials", methods=["GET"])
def get_client_credentials():
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload)
    access_token = response.json()
    session["client_code"] = access_token
    return response.json()


def valid_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.exceptions.HTTPError as err:
            print("\nEXCEPTION RAISED\n")
            if err.response.status_code == 401:
                print("Stale Token")
                get_client_credentials()

            return f(*args, **kwargs)

    return decorated_function

    # if session["auth_code"]:
    #     request.headers["Authorization"] = "Bearer" + session["auth_code"]
    # elif session["client_code"]:
    #     request.headers["Authorization"] = "Bearer" + session["client_code"]
    # else:
    #     token = access_token()["access_token"]
    #     request.headers["Authorization"] = "Bearer" + token

    # token = None
    # if "Authorization" not in request.headers:
    #     print("Authorization does not exist")

    # return f(*args, **kwargs)

    # x = 10
    # if x > 5:
    #     print("Token exists")
    # else:
    #     print("Token does not exist")
