import os


class Config:
    # absolute path of the base directory containing all files related to the project
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # directory containing blog articles
    ARTICLES_DIR = os.path.join(BASE_DIR, 'data', 'articles')
