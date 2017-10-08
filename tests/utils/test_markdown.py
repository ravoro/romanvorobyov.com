from unittest.mock import patch, mock_open

from app.utils.markdown import read_markdown_file
from tests import BaseCase


class Test(BaseCase):
    def test_convert_file(self):
        """Read a markdown file and convert it to a (html, meta) tuple."""
        mock_markdown = '{}\n{}'.format('title: Sample', 'sample **content**')

        with patch('builtins.open', mock_open(read_data=mock_markdown)) as _:
            html, meta = read_markdown_file('/path/to/sample.md')

        assert html == '<p>sample <strong>content</strong></p>'
        assert meta == {'title': 'Sample'}

    def test_convert_table(self):
        """Add 'table' class to HTML tables."""
        mock_markdown = '{}\n{}'.format(
            'Col1 | Col2',
            '---- | ----',
            'aaaa | bbbb',
            'cccc | dddd'
        )

        with patch('builtins.open', mock_open(read_data=mock_markdown)) as _:
            html, _ = read_markdown_file('/path/to/sample.md')

        assert '<table>' not in html
        assert '<table class="table">' in html

    def test_convert_meta_empty(self):
        """Convert empty lists in meta values to None."""
        mock_markdown = '{}\n{}'.format('title: ', 'sample **content**')

        with patch('builtins.open', mock_open(read_data=mock_markdown)) as _:
            _, meta = read_markdown_file('/path/to/sample.md')

        assert meta['title'] != []
        assert meta['title'] is None

    def test_convert_meta_single(self):
        """Convert single item lists in meta values to unwrapped items."""
        mock_markdown = '{}\n{}'.format('title: Sample', 'sample **content**')

        with patch('builtins.open', mock_open(read_data=mock_markdown)) as _:
            _, meta = read_markdown_file('/path/to/sample.md')

        assert meta['title'] != ['Sample']
        assert meta['title'] == 'Sample'

    def test_convert_meta_multiple(self):
        """Keep meta values with multi-item lists unchanged."""
        mock_markdown = '{}\n{}'.format('title: Sample\n    Another sample', 'sample **content**')

        with patch('builtins.open', mock_open(read_data=mock_markdown)) as _:
            _, meta = read_markdown_file('/path/to/sample.md')

        assert meta['title'] != ['Sample']
        assert meta['title'] == ['Sample', 'Another sample']
