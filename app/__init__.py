from flask import Flask

from .config import Config as app_config

app = Flask(__name__)
app.config.from_object(app_config)

from . import _handle_errors
from . import _url_trailing_slash
from . import controllers
