import requests
BASE_SITE = 'http://web:8000/'


def test_users_list(get_token_test):
    response = requests.get(
        url=BASE_SITE + 'api/v1/users/',
        headers={
            "Authorization": "Bearer "+get_token_test.get("access")
        },

    )
    assert response.status_code == 200
    assert response.json() != []


def test_delete_user_api(create_test_user, get_token_test):
    response = requests.delete(
        url=BASE_SITE + f'api/v1/users/{create_test_user}',
        headers={
            "Authorization": "Bearer " + get_token_test.get("access")
        },

    )
    assert response.status_code == 204
