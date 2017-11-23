from unittest.mock import patch, Mock

from app.controllers import blog_index
from app.repositories import ArticleRepo, Article
from tests import BaseCase, response_html


class Test(BaseCase):
    def setUp(self):
        super().setUp()
        blog_index.cache_clear()

    @patch.object(ArticleRepo, 'all')
    def test_ok(self, mock_all: Mock):
        """Return 200 and display a list of articles."""
        mock_result = [
            Article(title='A', url='/a', body='aaa'),
            Article(title='B', url='/b', body='bbb'),
            Article(title='C', url='/c', body='ccc'),
        ]
        mock_all.return_value = mock_result

        response = self.http.get('/blog')
        html = response_html(response)
        links = html.select('#page-content ul li a')

        assert response.status_code == 200
        for i, _ in enumerate(links):
            assert links[i].text == mock_result[i].title
            assert links[i].attrs['href'] == mock_result[i].url

    @patch.object(ArticleRepo, 'all')
    def test_empty(self, mock_all: Mock):
        """Return 200 and display a warning message when no articles are found."""
        mock_all.return_value = []

        response = self.http.get('/blog')
        html = response_html(response)
        links = html.select('#page-content ul li a')

        assert response.status_code == 200
        assert len(links) == 0
        assert 'No articles found.' in html.select_one('#page-content').text
