import pytest
import requests
import random
import string

BASE_URL = "https://stellarburgers.education-services.ru/api"

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@pytest.fixture
def user_data():
    return {
        "email": f"{generate_random_string()}@yandex.ru",
        "password": generate_random_string(),
        "name": generate_random_string()
    }

@pytest.fixture
def created_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    access_token = response.json().get("accessToken")
    yield user_data, access_token
    if access_token:
        requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": access_token})

@pytest.fixture
def valid_ingredient():
    response = requests.get(f"{BASE_URL}/ingredients")
    ingredients = response.json().get("data", [])
    return ingredients[0]["_id"] if ingredients else None