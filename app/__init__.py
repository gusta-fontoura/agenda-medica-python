from flask import Flask, session, redirect, url_for, request
from app.config import Config
from app.models import db
from app.utils.logger import logger


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.api_mock import api_mock_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_mock_bp)

    @app.before_request
    def require_login():
        allowed_routes = ["auth.login", "static", "api_mock.get_agendamentos"]
        if (
            "user_id" not in session
            and request.endpoint
            and request.endpoint not in allowed_routes
            and not request.endpoint.startswith("api_mock")
        ):
            return redirect(url_for("auth.login"))

    logger.info("Aplicacao Agenda Medica inicializada com sucesso.")
    return app
