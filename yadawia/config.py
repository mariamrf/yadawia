from yadawia import app
import os

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY = 'secret key'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
MAX_PHOTO_SIZE = 10
CSRF_ENABLED = True