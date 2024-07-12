from fastapi import APIRouter, Response, Request, Query, Header

from schemas.users import User, Registry, Login
from responses.users import UserNotFound, UserAlreadyExist
from database.sql import cur, commit


router = APIRouter(prefix="/users")


@router.post("/sigin", responses={401: dict(model=UserNotFound)})
async def sigin(
    login: Login, 
    request: Request, 
    response: Response
    ):

    verify =  login.verify()

    if verify: 
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