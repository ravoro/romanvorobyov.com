import os


class BaseConfig:
    DEBUG = False
    TESTING = False

    # absolute path of the base directory containing all files related to the project
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # directory containing blog articles
    ARTICLES_DIR = os.path.join(BASE_DIR, 'data', 'articles')


class ProdConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
