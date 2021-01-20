import os

BASE_SITE = os.environ.get('BASE_URL')


def test_users_list(api_client, get_token_test):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_token_test}')
    response = api_client.get(
        path=f'{BASE_SITE}/api/v1/users/',
    )
    assert response.status_code == 200
    assert response.json() != []


def test_delete_user_api(api_client, create_test_user, get_token_test):

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_token_test}')

    response = api_client.delete(
        path=f'{BASE_SITE}/api/v1/users/{create_test_user}/',
    )
    assert response.status_code == 204
