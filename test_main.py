import pytest
from fastapi.testclient import TestClient
from src.routes.root import router

# Setup the TestClient for FastAPI
client = TestClient(router)

@pytest.mark.parametrize(
    "test_id",
    [
        ("happy_path_default_message"),
        ("edge_case_empty_message"),
        ("error_case_invalid_method"),
    ]
)
def test_root(test_id):
    # Act
    if test_id == "happy_path_default_message":
        response = client.get("/")
    elif test_id == "edge_case_empty_message":
        response = client.get("/?message=")
    elif test_id == "error_case_invalid_method":
        response = client.post("/")  # Intentionally using the wrong method

    # Assert
    if test_id == "happy_path_default_message":
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}
    elif test_id == "edge_case_empty_message":
        assert response.status_code == 200
        assert response.json() != {"message": ""}
    elif test_id == "error_case_invalid_method":
        assert response.status_code == 405  # Method Not Allowed


