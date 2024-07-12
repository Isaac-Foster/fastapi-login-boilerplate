from fastapi import APIRouter, FastAPI
from app.routers import users


router = APIRouter(prefix='/api')

def init_app(app):
    router.include_router(users.router)
    app.include_router(router)