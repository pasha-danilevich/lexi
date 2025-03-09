# app/main.py
from fastapi import FastAPI

from api.router import router
from db.database import setup_database
from config import api

app = FastAPI()

# Настройка базы данных


if __name__ == "__main__":
    import uvicorn

    setup_database(app)
    app.include_router(router)

    uvicorn.run(app, host=api.SERVER_HOST, port=api.SERVER_PORT)
