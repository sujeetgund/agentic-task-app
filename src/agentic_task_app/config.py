import os
from dotenv import load_dotenv

load_dotenv()

DB_MODE = os.getenv("DB_MODE", "dev")  # "dev" or "prod"

TEXT_EXTRACTOR_AGENT_MODEL_ID = os.getenv("TEXT_EXTRACTOR_AGENT_MODEL_ID", "groq")

