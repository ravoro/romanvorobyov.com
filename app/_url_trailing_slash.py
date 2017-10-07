"""Redirect requests with a trailing slash to a url without trailing slash."""

from flask import redirect, request

from . import app

app.url_map.strict_slashes = False


@app.before_request
def remove_trailing_slash():
    path = request.path
    if path != '/' and path.endswith('/'):
        return redirect(path.rstrip('/'))
