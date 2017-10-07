"""Apply a generic custom template for http errors."""

from flask import Response, render_template
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES

from . import app


def handle_error(e: HTTPException) -> Response:
    return render_template('error.html', code=e.code, description=e.description)


for code in HTTP_STATUS_CODES:
    try:
        app.register_error_handler(code, handle_error)
    except KeyError:
        pass  # ignore rare exceptions that flask does not provide default handlers for
