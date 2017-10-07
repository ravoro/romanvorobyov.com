import os
from collections import namedtuple
from typing import Optional, List

from flask import current_app

from .utils.markdown import read_markdown_file

Article = namedtuple('Article', 'title, url, body')


class ArticleRepo:
    @staticmethod
    def all() -> List[Article]:
        """Return all articles, sorted in reverse chronological order."""
        basenames_unsorted = os.listdir(current_app.config['ARTICLES_DIR'])
        basenames = sorted(basenames_unsorted, reverse=True)
        return [ArticleRepo.get(b) for b in basenames]

    @staticmethod
    def get(basename: str) -> Optional[Article]:
        """Return details about the article identified by `basename`."""
        path = os.path.join(current_app.config['ARTICLES_DIR'], basename)
        if not os.path.isfile(path):
            return None
        html, meta = read_markdown_file(path)
        slug = os.path.splitext(basename)[0]
        return Article(
            title=meta.get('title'),
            url='/blog/{}'.format(slug),
            body=html
        )
