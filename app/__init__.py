from flask import Config, Flask


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    from ._handle_errors import app_handle_errors
    app = app_handle_errors(app)

    from ._url_trailing_slash import app_url_trailing_slash
    app = app_url_trailing_slash(app)

    from .controllers import bp as controllers
    app.register_blueprint(controllers)

    return app
