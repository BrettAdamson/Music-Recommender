import requests
from app.api import bp
from app.auth import auth
from flask import session
from app.auth.auth import token_required


@bp.route("/getdata")
@token_required
def getdata():
    return "<h1> Get Data </h1>"

    # if session["client_credentials"]:
    #     print("CREDENTIALS: \n")
    #     print(session["client_code"])
    #     print("\n")
    # elif session["auth_code"]:
    #     print("CREDENTIALS: \n")
    #     print(session["auth_code"])
    #     print("\n")


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
