import os

import dotenv

dotenv.load_dotenv()

MYSQL_HOST = os.getenv()
MYSQL_USERNAME = os.getenv()
MYSQL_PASSWORD = os.getenv()
MYSQL_DB = os.getenv()
MYSQL_DOC_LIMIT = 10000