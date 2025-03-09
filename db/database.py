from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

models = [
    "domain.user",
]


def setup_database(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": models},
        generate_schemas=True,
        add_exception_handlers=True,
    )
