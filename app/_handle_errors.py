"""Apply a generic custom template for http errors."""

from flask import Flask, Response, render_template
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES


# Use this function to add new app functionality, due to difficulties doing the same with Blueprints
def app_handle_errors(app: Flask) -> Flask:
    def handle_error(e: HTTPException) -> Response:
        return render_template('error.html', code=e.code, description=e.description)

    for code in HTTP_STATUS_CODES:
        try:
            app.register_error_handler(code, handle_error)
        except KeyError:
            pass  # ignore rare exceptions that flask does not provide default handlers for

    return app
