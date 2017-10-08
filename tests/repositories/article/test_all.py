import os
from unittest.mock import patch, Mock

from app.repositories import ArticleRepo, Article
from tests import BaseCase


class Test(BaseCase):
    def setUp(self):
        super().setUp()
        self.mock_articles_map = {
            '1.md': Article(title='A', url='/a', body='a a a'),
            '2.md': Article(title='B', url='/b', body='b b b'),
            '3.md': Article(title='C', url='/c', body='c c c'),
        }

    @patch.object(ArticleRepo, 'get')
    @patch.object(os, 'listdir')
    def test_all(self, mock_listdir: Mock, mock_get: Mock):
        """Return details about all articles in the listed dir."""
        mock_listdir.return_value = ['1.md', '2.md', '3.md']
        mock_get.side_effect = lambda x: self.mock_articles_map[x]

        with self.app.app_context():
            result = ArticleRepo.all()

        assert len(result) == 3

    @patch.object(ArticleRepo, 'get')
    @patch.object(os, 'listdir')
    def test_order(self, mock_listdir: Mock, mock_get: Mock):
        """Return all articles in reverse alphanumeric order"""
        unordered_basenames = [
            ['1.md', '3.md', '2.md'],
            ['2.md', '3.md', '1.md'],
            ['3.md', '1.md', '2.md']
        ]
        for basenames in unordered_basenames:
            mock_listdir.return_value = basenames
            mock_get.side_effect = lambda x: self.mock_articles_map[x]

            with self.app.app_context():
                result = ArticleRepo.all()

            assert result[0].title == 'C'
            assert result[1].title == 'B'
            assert result[2].title == 'A'

    @patch.object(ArticleRepo, 'get')
    @patch.object(os, 'listdir')
    def test_none(self, mock_listdir: Mock, mock_get: Mock):
        """Return an empty list when there are no articles in the listed dir."""
        mock_listdir.return_value = []
        mock_get.side_effect = lambda x: self.mock_articles_map[x]

        with self.app.app_context():
            result = ArticleRepo.all()

        assert len(result) == 0
