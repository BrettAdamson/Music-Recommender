import requests
from app.api import bp
from flask import session
from app.auth.auth import valid_client_credentials, valid_auth_code


@bp.route("/session_reset")
def session_reset():

    session["auth_code"] = None
    session["client_code"] = None

    return "Session Reset"


@bp.route("/get_session")
def get_session():

    print("\n Print Session \n")
    print(session["auth_code"])
    print(session["client_code"])

    return "Print Session"


@bp.route("/test_client")
@valid_client_credentials
def test_client():

    bearerToken = "Bearer " + session["client_code"]["access_token"]
    print(bearerToken)
    response = requests.get(
        "https://api.spotify.com/v1/search?q=journey&type=artist",
        headers={"Authorization": bearerToken},
    )

    response.raise_for_status()
    return response.json()


@bp.route("/test_auth")
@valid_auth_code
def test_auth():
    bearerToken = "Bearer " + session["auth_code"]["access_token"]
    print(bearerToken)
    response = requests.get(
        "https://api.spotify.com/v1/me",
        headers={"Authorization": bearerToken},
    )

    response.raise_for_status()
    return response.json()


# @bp.route("/spotify_token", methods=["GET"])
# def access_token():
#     print("in access token")
#     payload = {
#         "grant_type": "client_credentials",
#         "client_id": client_id,
#         "client_secret": client_secret,
#     }
#     res = requests.post("https://accounts.spotify.com/api/token", data=payload)
#     print(res.text)
#     return res.text
