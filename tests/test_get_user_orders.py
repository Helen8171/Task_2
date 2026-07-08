import requests
from data import BASE_URL

class TestGetUserOrders:
    def test_get_user_orders_with_auth(self, created_user, valid_ingredient):
        _, access_token = created_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": [valid_ingredient]}
        requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
        response = requests.get(f"{BASE_URL}/orders", headers=headers)
        assert response.status_code == 200

    def test_get_user_orders_without_auth(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert response.status_code == 401