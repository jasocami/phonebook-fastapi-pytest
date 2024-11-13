from fastapi import FastAPI
from api.routers import router
from api.sql_engine import create_db_and_tables

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
