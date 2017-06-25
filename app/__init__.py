import os
from typing import Dict

from flask import abort, Flask, redirect, render_template, request, url_for
from jinja2.exceptions import TemplateNotFound

from .config import Config as app_config
from .utils import slug_regex

app = Flask(__name__, template_folder=app_config.TEMPLATES_DIR)
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
    articles_path = os.path.join(app.config['BASE_DIR'],
                                 app.config['APP_DIR'],
                                 app.config['TEMPLATES_DIR'],
                                 app.config['ARTICLES_DIR'])
    basenames_unsorted = os.listdir(articles_path)
    basenames = sorted(basenames_unsorted, reverse=True)
    articles = [_article_meta(basename) for basename in basenames]
    return render_template('blog_index.html', articles=articles)


def _article_meta(basename: str) -> Dict[str, str]:
    """Return meta information about the article identified by `basename`."""
    template_path = os.path.join(app.config['ARTICLES_DIR'], basename)
    title = render_template(template_path,
                            hide_base=True,
                            hide_title=False,
                            hide_body=True)
    slug = os.path.splitext(basename)[0]
    url = '/blog/{}'.format(slug)
    return {
        'title': title,
        'url': url
    }


@app.route("/blog/<string:article>")
def blog_article(article: str):
    if not slug_regex.match(article):
        abort(400)
    try:
        return render_template('articles/{}.html'.format(article))
    except TemplateNotFound:
        abort(404)


@app.before_request
def remove_trailing_slash():
    """Redirect requests with a trailing slash to a url without trailing slash."""
    path = request.path
    if path != '/' and path.endswith('/'):
        return redirect(path.rstrip('/'))
