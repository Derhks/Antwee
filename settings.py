import os
from dotenv import load_dotenv
from utils.utils import check_boolean_string


load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = check_boolean_string(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))
URL_ANIMES = os.environ['URL_ANIMES']
URL_MORE_DATA = os.environ['URL_MORE_DATA']
ERROR_MESSAGE = os.environ['ERROR_MESSAGE']
TESTING = check_boolean_string(os.getenv('TESTING'))
