from fastapi import FastAPI
from app.routers import init_app

app = FastAPI()

init_app(app)