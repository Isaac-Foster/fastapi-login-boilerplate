import uuid

from fastapi import APIRouter, Response, Request, Query, Header

from app.schemas.users import User, Registry, Login
from app.responses.users import UserNotFound, UserAlreadyExist
from app.database.sql import cur, commit


router = APIRouter(prefix="/users")

session = dict()


@router.post("/sigin", responses={401: dict(model=UserNotFound)})
async def sigin(
    login: Login, 
    request: Request, 
    response: Response
    ):
    
    verify = login.verify()

    if verify: 
        session_id = uuid.uuid4()
        
        response.set_cookie("session", session_id)

        session[str(session_id)] = dict(user=login.username, passwd=login.passwd)

        return login

    return UserNotFound()


@router.post("/signup")
async def signup(
    registry: Registry, 
    request: Request, 
    response: Response
    ):

    if registry.register():
        return registry
    
    return UserAlreadyExist()