from flask import Blueprint


website = Blueprint("website", __name__)


@website.route("/blueprint")
def web_index():
    return "<h1>Welcome to website blueprint</h1>"
