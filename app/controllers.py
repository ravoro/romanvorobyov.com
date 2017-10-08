from flask import abort, Blueprint, redirect, render_template, Response, url_for

from .repositories import ArticleRepo
from .utils import slug_regex

bp = Blueprint('controllers', __name__)


@bp.route("/")
def home() -> Response:
    return redirect(url_for('controllers.blog_index'))


@bp.route("/about")
def about() -> Response:
    return render_template('about.html')


@bp.route("/contact")
def contact() -> Response:
    return render_template('contact.html')


@bp.route("/blog")
def blog_index() -> Response:
    articles = ArticleRepo.all()
    return render_template('blog_index.html', articles=articles)


@bp.route("/blog/<string:slug>")
def blog_article(slug: str) -> Response:
    if not slug_regex.match(slug):
        return abort(400)
    basename = '{}.md'.format(slug)
    article = ArticleRepo.get(basename)
    if not article:
        return abort(404)
    return render_template('base.html', **article._asdict())
