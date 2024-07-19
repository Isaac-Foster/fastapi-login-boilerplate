from http import HTTPStatus

from fastapi.testclient import TestClient
from app.main import app


async def test_registry_created_ok():
    client = TestClient(app)
    
    response = client.post(
        url="/api/users/signup",
        json=dict(
            name="user test test",
            email="sample@sample.com",
            username="usertest",
            passwd="SenhaTest21@#"
            )
        )

    assert response.status_code == HTTPStatus.CREATED


async def test_login_is_ok():
    client = TestClient(app)
    
    response = client.post(
        url="/api/users/signin",
        json=dict(
            username="usertest",
            passwd="SenhaTest21@#"
            )
        )

    assert response.status_code == HTTPStatus.OK


async def test_who_is_ok():
    client = TestClient(app)

    client.post(
        url="/api/users/signin",
        json=dict(
            username="usertest",
            passwd="SenhaTest21@#"
            )
        )

    response = client.get(url="/api/users/user")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == dict(message="tem session")
    