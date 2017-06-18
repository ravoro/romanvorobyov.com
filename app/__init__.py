from flask import abort, Flask, redirect, render_template, request, url_for
from jinja2.exceptions import TemplateNotFound

from .utils import slug_regex

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return redirect(url_for('about'))


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


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
