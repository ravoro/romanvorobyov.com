import os
from typing import Dict

from flask import abort, Flask, redirect, render_template, request, url_for, Response
from werkzeug.exceptions import HTTPException, HTTP_STATUS_CODES

from .config import Config as app_config
from .utils import slug_regex
from .utils.markdown import read_markdown_file

app = Flask(__name__)
app.config.from_object(app_config)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return redirect(url_for('blog_index'))


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/blog")
def blog_index():
    articles_path = os.path.join(app.config['ARTICLES_DIR'])
    basenames_unsorted = os.listdir(articles_path)
    basenames = sorted(basenames_unsorted, reverse=True)
    articles = [_article_meta(basename) for basename in basenames]
    return render_template('blog_index.html', articles=articles)


def _article_meta(basename: str) -> Dict[str, str]:
    """Return meta information about the article identified by `basename`."""
    path = os.path.join(app.config['ARTICLES_DIR'], basename)
    _, meta = read_markdown_file(path)
    slug = os.path.splitext(basename)[0]
    return {
        'title': meta.get('title'),
        'url': '/blog/{}'.format(slug)
    }


@app.route("/blog/<string:article>")
def blog_article(article: str):
    if not slug_regex.match(article):
        abort(400)
    try:
        path = os.path.join(app.config['ARTICLES_DIR'], article + '.md')
        html, meta = read_markdown_file(path)
        return render_template('base.html', body=html, **meta)
    except FileNotFoundError:
        abort(404)


@app.before_request
def remove_trailing_slash():
    """Redirect requests with a trailing slash to a url without trailing slash."""
    path = request.path
    if path != '/' and path.endswith('/'):
        return redirect(path.rstrip('/'))


for code in HTTP_STATUS_CODES:
    try:
        def handle_error(e: HTTPException) -> Response:
            return render_template('error.html', code=e.code, description=e.description)


        app.register_error_handler(code, handle_error)
    except KeyError:
        pass  # ignore rare exceptions that flask does not provide default handlers for
