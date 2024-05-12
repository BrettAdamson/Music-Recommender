from flask import Flask
from config import Config


def create_app(config_class=Config):
    from .api.routes import api

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api)

    from app.website import bp as website_bp

    app.register_blueprint(website_bp)

    return app
