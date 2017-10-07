from werkzeug.exceptions import abort

from tests import BaseCase
from tests.utils import response_html


class Test(BaseCase):
    def setUp(self):
        super().setUp()

        # sample endpoint for aborting with the specified error code
        @self.app.route('/sample-error-endpoint-<int:code>')
        def f(code: int) -> None:
            abort(code)

    def test_errors_common(self):
        """Return a custom HTML template for common http error codes."""
        common_errors = [400, 401, 403, 404, 408, 500, 502, 503]
        for code in common_errors:
            response = self.http.get('/sample-error-endpoint-{}'.format(code))
            html = response_html(response)
            assert response.status_code == code
            assert 'Sorry, an error occured... | Roman Vorobyov' == html.select_one('title').text
            assert str(code) in html.select_one('#page-content').text

    def test_errors_rare(self):
        """Raise LookupError and do not return a custom HTML template for rare http error codes."""
        rare_errors = [402, 449, 507, 510]
        for code in rare_errors:
            with self.assertRaises(LookupError):
                self.http.get('/sample-error-endpoint-{}'.format(code))
