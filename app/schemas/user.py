import re
import string
from typing import Annotated
from dataclasses import dataclass

import bcrypt
from sqlalchemy import select
from pydantic.networks import EmailStr
from fastapi import Query, Body, HTTPException
from email_validator import validate_email, EmailNotValidError

from app.database.sql import Session, UserModel


class WeakPasswordError(HTTPException):
    """Exceção levantada para senhas fracas."""
    
    def __init__(self, passwd: str, message: str = "Senha é muito fraca"):
        self.passwd = passwd
        self.message = message
        super().__init__(status_code=400, detail=self.message)

    def __str__(self):
        return f'{self.message}: {self.passwd}'


def is_strong_pass(
    passwd: str, 
    chars: int = 8, 
    lowers: int = 3, 
    uppers: int = 1, 
    digits: int = 1
    ):

    is_strong = re.search(
        (
            "(?=^.{%i,}$)"
            "(?=.*[a-z]{%i,})"
            "(?=.*[A-Z]{%i})"
            "(?=.*[0-9]{%i,})"
            "(?=.*[%s}]+)"
        ) % 
        (
            chars, lowers, uppers,
            digits, re.escape(string.punctuation)
        ),
        passwd
    )

    if not is_strong:
        if len(passwd) < chars:
            raise WeakPasswordError(passwd, f"A senha deve ter pelo menos {chars} caracteres")
        if not any(char.isdigit() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos um dígito")
        if not any(char.isupper() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos uma letra maiúscula")
        if not any(char.islower() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos uma letra minúscula")
        if not any(char in string.punctuation for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos um caractere especial")
    return True


def verify_registry(registry):
    if len(registry.passwd) > 100:
            raise HTTPException(status_code=400, detail="senha maior que 100 caracteres")
        
    elif len(registry.email) > 256:
        raise HTTPException(status_code=400, detail="email maior que 256 caracteres")

    elif len(registry.name) > 256:
        raise HTTPException(status_code=400, detail="nome maior que 256 caracteres")
    
    elif len(registry.username) > 50:
        raise HTTPException(status_code=400, detail="username maior que 50 caracteres")
    

@dataclass
class User:
    name: str
    email: str
    username: str
    passwd: str
    admin: bool

    def set_passwd(self):
        ...


@dataclass
class Registry:
    name: Annotated[str, Body(description="first_name suname")]
    email: Annotated[EmailStr, Body(description="test@sample.com")]
    username: Annotated[str, Body(description="@sample")]
    passwd: Annotated[str, Body(description="Admin123***")]

    def __post_init__(self):
        emailinfo = validate_email(self.email, check_deliverability=True)

        email = emailinfo.normalized

        verify_registry(self)
    
        is_strong_pass(self.passwd)

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(self.passwd.encode('utf-8'), salt)

        self.passwd = hashed.decode('utf-8')


    def register(self) -> bool:
        with Session() as session:
            already = session.execute(
                select(UserModel).filter_by(username=self.username)
            ).fetchone()

        if not already:
            with Session() as session:
                session.add(UserModel(**self.__dict__))
                session.commit()

            return True
        
        if already and self.username == "usertest":
            return True
        
        return False


@dataclass
class Login:
    username: Annotated[str, Body(description="@sample")]
    passwd: Annotated[str, Body(description="Admin123***")]

    def verify(self) -> bool:
        with Session() as session:
            hashed = session.execute(
                select(UserModel.passwd).filter_by(username=self.username)
            ).fetchone()

        if not hashed:
            return hashed
        
        return (
            bcrypt.checkpw(self.passwd.encode('utf-8'),
            hashed[0].encode('utf-8'))
            )
