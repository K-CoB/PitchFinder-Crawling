import os

import dotenv

dotenv.load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST", '127.0.0.1')
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", 'root')
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", '')
MYSQL_DB = os.getenv('MYSQL_DB', 'pitchfinder')
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
MYSQL_DOC_LIMIT = 10000