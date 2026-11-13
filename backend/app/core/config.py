from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Receipt Scanner API"
    environment: str = "development"

    database_url: str = ""

    secret_key: str = ""
    access_token_expire_minutes: int = 60

    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_model: str = ""

    upload_dir: str = "uploads"
    max_upload_mb: int = 10
    max_pdf_pages: int = 3

    cors_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
