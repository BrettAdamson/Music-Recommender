from flask import Flask
from config import Config


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.core import bp as core_bp

    app.register_blueprint(core_bp)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp)

    return app
