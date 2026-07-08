import requests
from data import BASE_URL
from helpers import generate_random_string

class TestUpdateUser:
    def test_update_user_with_auth(self, created_user):
        _, access_token = created_user
        new_data = {"email": f"{generate_random_string()}@yandex.ru", "name": generate_random_string()}
        headers = {"Authorization": access_token}
        response = requests.patch(f"{BASE_URL}/auth/user", json=new_data, headers=headers)
        assert response.status_code == 200

    def test_update_user_without_auth(self):
        new_data = {"email": f"{generate_random_string()}@yandex.ru"}
        response = requests.patch(f"{BASE_URL}/auth/user", json=new_data)
        assert response.status_code == 401