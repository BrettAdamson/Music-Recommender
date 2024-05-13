from flask import Flask
from config import Config


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.website import bp as website_bp

    app.register_blueprint(website_bp)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp)

    return app
