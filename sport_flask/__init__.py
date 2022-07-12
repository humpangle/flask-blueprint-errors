# -*- coding: utf-8 -*-

from flask import Flask

from .routes.health import health_bp
from .routes.users import users_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
