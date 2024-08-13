from fastapi import APIRouter, Request, responses, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.database.redis import login_required, redis_manager

router = APIRouter(tags=["view"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/", name="signin")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request":  request})


@router.get("/signup", name="register")
async def signup(request: Request):
    return templates.TemplateResponse("register.html", {"request":  request})


@router.get("/profile")
async def signup(request: Request):
    return templates.TemplateResponse("logout.html", {"request":  request})


@router.get("/logout")
@login_required
async def logout(request: Request, response: Response):
    session = request.cookies.get("session")
    response.set_cookie(key="session")

    if session and redis_manager.exists(session):
        redis_manager.delete(session)

    return responses.RedirectResponse(url="/")