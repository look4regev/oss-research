import os

from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
TOP_PERCENT_OWNERS = 0.029
TOP_PERCENT_REPOSITORIES = 0.014
