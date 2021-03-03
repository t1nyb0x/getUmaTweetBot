import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.environ.get('ACCESS_SECRET_TOKEN')
API_KEY = os.environ.get('API_KEY')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
UMA_MUSU_TWITTERID = os.environ.get('UMA_MUSU_TWITTERID')
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
