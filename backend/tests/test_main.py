from starlette.testclient import TestClient


def test_root(client:TestClient):
    response = client.get('/')
    data = {"message": "Hello World"}
    assert response.status_code == 200
    assert response.json() == data