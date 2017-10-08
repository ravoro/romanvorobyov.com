import os
from unittest.mock import patch, Mock

from app.repositories import ArticleRepo, Article
from tests import BaseCase


class Test(BaseCase):
    @patch('app.repositories.read_markdown_file')
    @patch.object(os.path, 'isfile')
    def test_ok(self, mock_isfile: Mock, mock_read: Mock):
        """Return details about the requested article."""
        mock_article = Article(title='Sample', url='/blog/sample', body='sample content')
        mock_isfile.return_value = True
        mock_read.return_value = (mock_article.body, {'title': mock_article.title})

        with self.app.app_context():
            result = ArticleRepo.get('sample.md')

        assert result == mock_article

    @patch.object(os.path, 'isfile')
    def test_not_found(self, mock_isfile: Mock):
        """Return None if the article can not be found."""
        mock_isfile.return_value = False

        with self.app.app_context():
            result = ArticleRepo.get('sample.md')

        assert result is None
