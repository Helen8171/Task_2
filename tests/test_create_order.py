import requests
from conftest import BASE_URL

class TestCreateOrder:
    def test_create_order_with_auth_and_ingredients(self, created_user, valid_ingredient):
        _, access_token = created_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": [valid_ingredient]}
        response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
        assert response.status_code == 200

    def test_create_order_without_auth_with_ingredients(self, valid_ingredient):
        payload = {"ingredients": [valid_ingredient]}
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        assert response.status_code == 200

    def test_create_order_without_ingredients(self, created_user):
        _, access_token = created_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": []}
        response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
        assert response.status_code == 400

    def test_create_order_invalid_hash(self, created_user):
        _, access_token = created_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": ["invalid_hash_123"]}
        response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
        assert response.status_code == 500