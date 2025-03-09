import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_PATH = Path(__file__).parent.parent


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_PATH, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
