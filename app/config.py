import os


class Config:
    # absolute path of the base directory containing all files related to the project
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # directory containing all Flask app files (relative to BASE_DIR)
    APP_DIR = 'app'

    # directory containing all Jinja templates (relative to APP_DIR)
    TEMPLATES_DIR = 'templates'

    # directory containing blog articles (relative to TEMPLATES_DIR)
    ARTICLES_DIR = 'articles'
