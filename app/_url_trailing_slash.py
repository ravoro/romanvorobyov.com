"""Redirect requests with a trailing slash to a url without trailing slash."""

from flask import Flask, redirect, request


# Use this function to add new app functionality, due to difficulties doing the same with Blueprints
def app_url_trailing_slash(app: Flask) -> Flask:
    app.url_map.strict_slashes = False

    @app.before_request
    def remove_trailing_slash():
        path = request.path
        if path != '/' and path.endswith('/'):
            return redirect(path.rstrip('/'))

    return app
