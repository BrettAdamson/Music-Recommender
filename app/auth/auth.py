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


@bp.route("/auth_code")
def get_oauth_token():
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


@bp.route("/refresh_token", methods=["GET"])
def refresh_token():
    print(session["auth_code"]["refresh_token"])
    response = requests.post(
        TOKEN_URL,
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        data={
            "grant_type": "refresh_token",
            "refresh_token": session["auth_code"]["refresh_token"],
        },
    )
    auth_token = response.json()

    session["auth_code"] = auth_token
    return response.json()


def valid_auth_code(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if session.get("auth_code") is None:
                print("IN DECORATOR")
                get_oauth_token()
            return f(*args, **kwargs)
        except requests.exceptions.HTTPError as err:
            print("\nEXCEPTION RAISED\n")
            if err.response.status_code == 401:
                print("Stale Token. Using Refresh Token")
                refresh_token()
            return f(*args, **kwargs)

    return decorated_function


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


def valid_client_credentials(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if session.get("client_code") is None:
                get_client_credentials()
            return f(*args, **kwargs)
        except requests.exceptions.HTTPError as err:
            print("\nEXCEPTION RAISED\n")
            if err.response.status_code == 401:
                print("Stale Token. Getting New Client Credentials")
                get_client_credentials()

            return f(*args, **kwargs)

    return decorated_function
