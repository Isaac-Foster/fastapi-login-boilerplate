import uuid

from fastapi import APIRouter, Response, Request, Query, Header, responses

from app.schemas.user import User, Registry, Login
from app.responses.users import (
    UserNotFound, 
    UserAlreadyExist, 
    LoginSucessfull, 
    RegistrySuccessful
)

from app.database.redis import redis_manager, login_required


router = APIRouter(prefix="/users", tags=["api"])


@router.post("/signin", responses={
    200: dict(model=LoginSucessfull),
    401: dict(model=UserNotFound)
    }, name="login")
async def signin(
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
    },
    name="signup"
    )
async def signup(
    registry: Registry, 
    request: Request, 
    response: Response
    ):
    print(registry)
    if registry.register():
        response.status_code = 201
        return RegistrySuccessful()
    response.status_code = 303
    return UserAlreadyExist()


@router.get("/user")
@login_required
async def who(request: Request, response: Response):
    return dict(message="tem session")
