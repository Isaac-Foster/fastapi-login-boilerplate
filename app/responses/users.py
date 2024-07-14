from pydantic import BaseModel


class LoginSucessfull(BaseModel):
    message: str = "Logado com sucesso."

class Unauthorized(BaseModel):
    message: str = "você não tem permissão"

class ResultNotFound(BaseModel):
    message: str = "resultado não encontrado"

class UserNotFound(BaseModel):
    message: str = "Usuário não encontrado"

class RegistrySuccessful(BaseModel):
    message: str = "Usuário registrado com sucesso."

class UserAlreadyExist(BaseModel):
    message: str = "Usuário já existente"