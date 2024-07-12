from fastapi import APIRouter, FastAPI
from routers import users


router = APIRouter(prefix='/api')

def init_app(app):
    router.include_router(users.router)
    app.include_router(router)