import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "klucz_nie_do_zlamania"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
