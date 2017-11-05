from unittest import TestCase

from bs4 import BeautifulSoup
from flask import Response

import config
from app import create_app


class BaseCase(TestCase):
    def setUp(self):
        self.app = create_app(config.TestConfig)
        self.http = self.app.test_client()


def response_html(response: Response) -> BeautifulSoup:
    """Return response body as parsed html (i.e. BeautifulSoup object)."""
    return BeautifulSoup(response.get_data(as_text=True), 'html.parser')
