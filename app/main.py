from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello World!</p>"


def home():
    return render_template("home.html")


@app.route("/index")
def index():
    return "<p>Index Page</p>"
