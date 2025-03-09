from functools import lru_cache
from typing import List

from pydantic import Field

from config.base import Base


class AppUse(Base):
    USE_AUTH: bool = True
    USE_GRPC_AUTH: bool = False
    USE_LOGS_MIDDLEWARE: bool = True
    USE_BG_LOGS_TO_ES: bool = False
    USE_SEND_TO_ELASTIC: bool = False


class API(Base):
    ALLOWED_HOSTS: List[str] = Field(default=["*"])
    API_KEY: str
    AUTH_URL: str = "http://127.0.0.1:7101/auth/token"
    DEBUG: bool = Field(default=False, alias="debug")
    ENVIRONMENT: str = "dev"
    OPENAPI_URL: str = "/openapi.json"
    PROJECT_NAME: str = Field(default="Lexi", alias="title")
    PROJECT_DESCRIPTION: str = Field(default="Backend", alias="description")
    ROOT_PREFIX: str
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 7102
    APP_WORKERS: int = Field(default=1)


@lru_cache()
def get_app_use_settings() -> AppUse:
    return AppUse()


@lru_cache()
def get_api_settings() -> API:
    return API()
