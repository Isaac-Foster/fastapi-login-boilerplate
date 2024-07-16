from http import HTTPStatus

from fastapi.testclient import TestClient
from app.main import app



async def test_registry_is_ok():
    client = TestClient(app)
    
    response = client.post(
        url="/api/users/singin",
        json=dict(
            name="vey da havan",
            email="sample@sample.com",
            username="usertest",
            passwd="Senha21@#"
        )
        )

    assert response.status_code == HTTPStatus.CREATED
    