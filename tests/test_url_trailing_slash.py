from tests import BaseCase


class Test(BaseCase):
    def setUp(self):
        super().setUp()

    def test_no_slash(self):
        """Do not redirect to a url ending with a slash, when given a url with no ending slash."""

        @self.app.route('/sample-endpoint')
        def f():
            return '', 200

        response = self.http.get('/sample-endpoint')
        assert response.status_code == 200
        assert response.status_code not in range(300, 400)
        assert response.headers.get('location') is None

    def test_end_slash(self):
        """Redirect to a url not ending with a slash, when given a url with an ending slash."""

        @self.app.route('/sample-endpoint/')
        def f():
            return '', 200

        response = self.http.get('/sample-endpoint/')
        assert response.status_code != 200
        assert response.status_code in range(300, 400)
        assert response.headers.get('location').endswith('/sample-endpoint')
