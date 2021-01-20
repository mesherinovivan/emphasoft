import os
import random
import pytest
from rest_framework.test import APIClient

BASE_SITE = os.environ.get('BASE_URL')
TEST_USER = os.environ.get('TEST_USER')
TEST_PASSWORD = os.environ.get('TEST_PASSWORD')


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_dbfile.sqlite3',
    }


@pytest.fixture(scope='session')
def api_client() -> APIClient:
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture(autouse=True)
def get_token_test(api_client, db) -> dict:
    response = api_client.post(
        path=f'{BASE_SITE}/api-token-auth/',
        data={
            "username": TEST_USER,
            "password": TEST_PASSWORD
        }
    )
    assert response.status_code == 200
    return response.json()["access"]


@pytest.fixture()
def create_test_user(api_client, get_token_test: dict) -> int:
    name_prefix = random.random()
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_token_test}')
    response = api_client.post(
        path=f'{BASE_SITE}/api/v1/users/',
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
