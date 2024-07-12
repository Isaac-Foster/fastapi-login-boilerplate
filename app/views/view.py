from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()


templates = Jinja2Templates(directory="templates")

@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request":  request})