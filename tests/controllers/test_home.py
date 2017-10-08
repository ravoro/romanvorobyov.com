from flask import url_for

from tests import BaseCase


class Test(BaseCase):
    def test_ok(self):
        """Return 302 and redirect to the blog index page."""
        response = self.http.get('/')
        assert response.status_code == 302
        with self.app.test_request_context():
            assert response.headers['location'].endswith(url_for('controllers.blog_index'))
