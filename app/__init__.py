from flask import Flask
from config import Config


def create_app(config_class=Config):
    from .api.routes import api
    from .website.routes import website

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api)
    app.register_blueprint(website)
    # from app import routes

    return app
