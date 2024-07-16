import uuid

from fastapi import APIRouter, Response, Request, Query, Header

from app.schemas.users import User, Registry, Login
from app.responses.users import (
    UserNotFound, 
    UserAlreadyExist, 
    LoginSucessfull, 
    RegistrySuccessful
)

from app.databases.redis import redis_manager, login_required


router = APIRouter(prefix="/users")


@router.post("/signin", responses={
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
            max_age=120
        )

        redis_manager.insert(key=session_id, time=120, value=login.username)
        response.status_code = 200
        return LoginSucessfull()
    response.status_code = 401
    return UserNotFound()


@router.post("/signup", responses={
    201: dict(model=RegistrySuccessful),
    303: dict(model=UserAlreadyExist)
    })
async def signup(
    registry: Registry, 
    request: Request, 
    response: Response
    ):

    if registry.register():
        response.status_code = 201
        return RegistrySuccessful()
    response.status_code = 303
    return UserAlreadyExist()


@router.delete("/logout")
@login_required
async def logout(request: Request, response: Response):
    redis_manager
    return


@router.get("/user")
@login_required
async def who(request: Request, response: Response):
    return dict(message="tem session")
