import os
from dotenv import load_dotenv

load_dotenv()

DB_MODE = os.getenv("DB_MODE", "dev")  # "dev" or "prod"
