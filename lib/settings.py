import os

import dotenv

dotenv.load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST", '127.0.0.1')
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", 'root')
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", '')
MYSQL_DB = os.getenv('MYSQL_DB', 'pitchfinder')
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
MYSQL_DOC_LIMIT = 10000