import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "klucz_nie_do_zlamania"
    API_KEY = "sa63K3JQBuY23fdtPM5Ub7JMFXyEilI8H6d72pMx"