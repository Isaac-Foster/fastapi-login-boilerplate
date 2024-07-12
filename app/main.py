from fastapi import FastAPI
from routers import init_app

app = FastAPI()

init_app(app)