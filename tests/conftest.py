import pytest
import requests
import pytest
import random
import os

BASE_SITE = os.environ.get('BASE_URL')
TEST_USER = os.environ.get('TEST_USER')
TEST_PASSWORD = os.environ.get('TEST_PASSWORD')


@pytest.fixture(scope="session", autouse=True)
def get_token_test() -> dict:
    response = requests.post(
       url=BASE_SITE + 'api-token-auth/',
       data={
            "username": TEST_USER,
            "password": TEST_PASSWORD
       }
    )
    assert response.status_code == 200
    return response.json()


@pytest.fixture(autouse=True)
def create_test_user(get_token_test: dict) -> int:
    name_prefix = random.random()

    response = requests.post(
        url=BASE_SITE + 'api/v1/users/',
        headers={
            "Authorization": "Bearer "+get_token_test.get("access")
        },
        data={
            "username": f"iamescherinov_test{name_prefix}",
            "first_name": "test",
            "last_name": "test",
            "password": "testtest",
            "is_active": True
        }

    )
    assert response.status_code == 201
    assert response.json() != []
    return response.json().get("id")
