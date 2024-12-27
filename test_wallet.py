import pytest
from database import Base, engine
from main import app
from config import TEST_ADDRESS


@pytest.fixture(scope="module")
def test_client():
    from fastapi.testclient import TestClient
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

def test_post_wallet_info(test_client):
    response = test_client.post("/wallet/", json={"address": TEST_ADDRESS})
    assert response.status_code == 200
    data = response.json()
    assert "address" in data and data["address"] == TEST_ADDRESS
    assert "balance" in data and data["balance"] >= 0
    assert "bandwidth" in data and data["bandwidth"] >= 0
    assert "energy" in data and data["energy"] >= 0

def test_get_wallet_queries(test_client):
    response = test_client.get("/wallet/queries/", params={"skip": 0, "limit": 5})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "address" in item
        assert "balance" in item
        assert "bandwidth" in item
        assert "energy" in item
        assert "queried_at" in item
