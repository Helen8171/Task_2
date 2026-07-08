import requests
import pytest
from data import BASE_URL

class TestCreateUser:
    def test_create_unique_user(self, user_data):
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True
        access_token = response.json().get("accessToken")
        if access_token:
            requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": access_token})

    def test_create_existing_user(self, created_user):
        user_data, _ = created_user
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 403

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, user_data, missing_field):
        user_data.pop(missing_field)
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 403