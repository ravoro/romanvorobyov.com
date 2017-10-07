from unittest import TestCase
from app import create_app, config


class BaseCase(TestCase):
    def setUp(self):
        self.app = create_app(config.TestConfig)
        self.http = self.app.test_client()
