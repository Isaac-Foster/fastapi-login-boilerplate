import uuid

from fastapi import APIRouter, Response, Request, Query, Header

from app.schemas.users import User, Registry, Login
from app.responses.users import (
    UserNotFound, 
    UserAlreadyExist, 
    LoginSucessfull, 
    ResgistrySucessfull
)
from app.database.sql import cur, commit
from app.database.redis import redis_manager, login_requeried


router = APIRouter(prefix="/users")


@router.post("/sigin", responses={
    200: dict(model=LoginSucessfull),
    401: dict(model=UserNotFound)
    })
async def sigin(
    login: Login, 
    request: Request, 
    response: Response
    ):
    
    verify = login.verify()

    if verify: 
        session_id = uuid.uuid4()
        response.set_cookie(
            key="session", 
            value=session_id, 
            httponly=True, 
            max_age=30
        )

        redis_manager.insert(key=session_id, time=30, value=login.username)

        return LoginSucessfull()

    return UserNotFound()


@router.post("/signup", responses={
    201: dict(model=ResgistrySucessfull),
    303: dict(model=UserAlreadyExist)
    })
async def signup(
    registry: Registry, 
    request: Request, 
    response: Response
    ):

    if registry.register():
        return ResgistrySucessfull()
    
    return UserAlreadyExist()


@router.get("/user")
@login_requeried
async def who(request: Request, response: Response):
    return dict(message="tem session")
