from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Agent MVP"
    openai_api_key: str
    openai_model: str = "gpt-4.1"
    slack_webhook_url: str | None = None

    datadog_api_key: str | None = None
    datadog_app_key: str | None = None
    datadog_site: str = "datadoghq.com"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()