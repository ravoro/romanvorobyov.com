from typing import Dict, List, Tuple, Union

from markdown import Markdown

md = Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.meta'])


def read_markdown_file(path: str) -> Tuple[str, Dict]:
    """Read markdown file identified by `path` and return the converted html and meta."""
    with open(path) as f:
        text = f.read()
    html_raw = md.convert(text)
    html = _convert_html(html_raw)
    meta_raw = md.Meta
    meta = {k: _convert_meta_value(v) for k, v in meta_raw.items()}
    return html, meta


def _convert_html(html: str) -> str:
    """Convert html such that:
        - a <table> tag is given a 'table' class
    """
    return html.replace('<table>', '<table class="table">')


def _convert_meta_value(v: List[str]) -> Union[None, str, List[str]]:
    """Convert meta values such that:
        - a list containing a single empty item is replaced with None
        - a list containing a single item is replaced with the single item (i.e. no list)
        - a list containing multiple items remains untouched
    """
    if len(v) == 1:
        if len(v[0]) == 0:
            return None
        return v[0]
    return v
