import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

UMA_MUSU_TWITTERID = os.environ.get('UMA_MUSU_TWITTERID')
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
BEARER = os.environ.get('API_BEARER')
HAL = os.environ.get('HAL')
NAKAKOMA = os.environ.get('NAKAKOMA')