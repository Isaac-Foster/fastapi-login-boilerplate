from pydantic import BaseModel


class Unauthorized(BaseModel):
    message: str = "você não tem permissão"

class ResultNotFound(BaseModel):
    message: str = "resultado não encontrado"

class UserNotFound(BaseModel):
    message: str = "Usuário não encontrado"


class UserAlreadyExist(BaseModel):
    message: str = "Usuário já existente"