from unittest.mock import patch, Mock

from app.repositories import ArticleRepo, Article
from tests import BaseCase, response_html


class Test(BaseCase):
    @patch.object(ArticleRepo, 'get')
    def test_ok(self, mock_get: Mock):
        """Return 200 and display the requested article."""
        mock_result = Article(title='A', url='/a', body='aaa')
        mock_get.return_value = mock_result

        response = self.http.get('/blog/a')
        html = response_html(response)

        assert response.status_code == 200
        assert html.select_one('#page-content h1').text == mock_result.title
        assert mock_result.body in html.select_one('#page-content').text

    @patch.object(ArticleRepo, 'get')
    def test_not_found(self, mock_get: Mock):
        """Return 404 and display an error page when the article can not be found."""
        mock_get.return_value = None

        response = self.http.get('/blog/non-existing-article')
        html = response_html(response)

        assert response.status_code == 404
        assert 'error' in html.select_one('#page-content h1').text
        assert '404' in html.select_one('#page-content').text

    def test_invalid_slug(self):
        """Return 400 and display an error page when given an invalid slug."""
        response = self.http.get('/blog/uh~oh~$$$~invalid')
        html = response_html(response)

        assert response.status_code == 400
        assert 'error' in html.select_one('#page-content h1').text
        assert '400' in html.select_one('#page-content').text
