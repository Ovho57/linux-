"""Application configuration loaded from environment variables."""
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    model: str = os.getenv("AI_MODEL", "deepseek/deepseek-chat")
    database: str = os.getenv("JAXO_DATABASE", "jaxo_history.sqlite3")

settings = Settings()
