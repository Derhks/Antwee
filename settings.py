import os
from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

URL_ANIMES = os.environ['URL_ANIMES']
URL_MORE_DATA = os.environ['URL_MORE_DATA']
ERROR_MESSAGE = os.environ['ERROR_MESSAGE']
