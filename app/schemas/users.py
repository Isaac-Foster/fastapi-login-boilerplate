import bcrypt

from typing import Annotated
from dataclasses import dataclass
from pydantic.networks import EmailStr
from email_validator import validate_email, EmailNotValidError


from fastapi import Query, Body
from app.database.sql import cur, commit


@dataclass
class User:
    name: Annotated[str, Body(description="first_name suname")]
    email: Annotated[str, Body(description="test@sample.com")]
    username: Annotated[str, Body(description="@sample")]
    passwd: Annotated[str, Body(description="Admin123***")]
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
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(self.passwd.encode('utf-8'), salt)
        self.passwd = hashed.decode('utf-8')

        emailinfo = validate_email(self.email, check_deliverability=True)

        email = emailinfo.normalized


    def register(self) -> bool:
        alerdy = cur.execute(
            "SELECT * FROM users WHERE username = ?",
            [self.username]
        ).fetchone()

        if not alerdy:
            cur.execute(
                "INSERT INTO users(name, email, username, passwd) VALUES(?, ?, ?, ?)",
                [self.name, self.email, self.username, self.passwd]
            )

            commit()

            return True
        
        return False


@dataclass
class Login:
    username: Annotated[str, Body(description="@sample")]
    passwd: Annotated[str, Body(description="Admin123***")]

    def verify(self) -> bool:
        hashed = cur.execute(
            "SELECT passwd FROM users WHERE username = ?",
            [self.username]
        ).fetchone()

        if not hashed:
            return hashed
        
        return (
            bcrypt.checkpw(self.passwd.encode('utf-8'),
            hashed[0].encode('utf-8'))
            )
