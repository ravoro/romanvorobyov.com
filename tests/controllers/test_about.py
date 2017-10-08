from tests import BaseCase, response_html


class Test(BaseCase):
    def test_ok(self):
        """Return 200 and display the about page."""
        response = self.http.get('/about')
        html = response_html(response)
        assert response.status_code == 200
        assert html.select_one('title').text == 'About | Roman Vorobyov'
