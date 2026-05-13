from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Smart Books Library Bot"
    app_env: str = "development"
    app_debug: bool = True
    secret_key: str = "change-me"

    database_url: str = Field(default="sqlite+aiosqlite:///./smart_books.db", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")

    bot_token: str = Field(default="", alias="BOT_TOKEN")
    bot_use_redis: bool = Field(default=False, alias="BOT_USE_REDIS")

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    admin_ids: str = Field(default="", alias="ADMIN_IDS")
    force_join_chat_id: str = Field(default="", alias="FORCE_JOIN_CHAT_ID")
    force_join_chat_link: str = Field(default="", alias="FORCE_JOIN_CHAT_LINK")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    @property
    def admin_id_list(self) -> List[int]:
        if not self.admin_ids.strip():
            return []
        values = []
        for item in self.admin_ids.split(','):
            item = item.strip()
            if item:
                try:
                    values.append(int(item))
                except ValueError:
                    continue
        return values


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
