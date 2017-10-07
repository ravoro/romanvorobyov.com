from bs4 import BeautifulSoup
from flask import Response


def response_html(response: Response) -> BeautifulSoup:
    """Return response body as parsed html (i.e. BeautifulSoup object)."""
    return BeautifulSoup(response.get_data(as_text=True), 'html.parser')
