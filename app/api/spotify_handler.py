import requests
from app.api import bp
from app.auth import auth
from flask import session
from app.auth.auth import valid_token


@bp.route("/test")
@valid_token
def getdata():
    # authToken = auth.get_client_credentials()

    bearerToken = "Bearer " + session["client_code"]["access_token"]
    print(bearerToken)
    response = requests.get(
        "https://api.spotify.com/v1/search?q=journey&type=artist",
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
