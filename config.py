import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "klucz_nie_do_zlamania"