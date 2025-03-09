from functools import lru_cache

from config.base import Base


class Postgres(Base):
    USER: str = "postgres"
    PASS: str = "postgres"
    HOST: str = "localhost"
    PORT: int = 15432
    NAME: str = "dbname"


@lru_cache()
def get_postgres_settings() -> Postgres:
    return Postgres()
