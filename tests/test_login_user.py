import requests
from data import BASE_URL

class TestLoginUser:
    def test_login_existing_user(self, created_user):
        user_data, _ = created_user
        login_payload = {"email": user_data["email"], "password": user_data["password"]}
        response = requests.post(f"{BASE_URL}/auth/login", json=login_payload)
        assert response.status_code == 200

    def test_login_wrong_credentials(self, created_user):
        user_data, _ = created_user
        login_payload = {"email": user_data["email"], "password": "wrong_password"}
        response = requests.post(f"{BASE_URL}/auth/login", json=login_payload)
        assert response.status_code == 401