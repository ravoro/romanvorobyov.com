from flask import Flask, redirect, render_template, request, url_for

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


@app.before_request
def trailing_slash():
    """Redirect requests with a trailing slash to a url without trailing slash."""
    path = request.path
    if path != '/' and path.endswith('/'):
        return redirect(path.rstrip('/'))
