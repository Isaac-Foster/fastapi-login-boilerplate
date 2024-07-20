from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", name="signin")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request":  request})


@router.get("/signup", name="signup")
async def root(request: Request):
    return templates.TemplateResponse("register.html", {"request":  request})