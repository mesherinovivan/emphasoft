import json
import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestUser(TestCase):

    def setUp(self):
        user_data = {"username": "testuser", "password": "test"}
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            **user_data
        )
        response = self.client.post(reverse('token_obtain_pair'), data=user_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None
        assert len(response.json()) == 2
        assert "access" in response.json()

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.json()["access"]}')

    def test_create_user_api(self):
        user_data = {
            "username": "testtest", "first_name": "test",
            "last_name": "test", "password": "testtest",
            "is_active": False
        }
        response = self.client.post(
            reverse("api:user-list"),
            data=user_data
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_user_api(self):
        response = self.client.get(reverse("api:user-list"))
        assert response.status_code == status.HTTP_200_OK
        assert response.json() != []

    def test_update_user_api(self):
        update_user = get_user_model().objects.last()
        user_data = {
            "is_active": True
        }
        response = self.client.patch(
            reverse("api:user-detail", args=[update_user.pk]),
            user_data
        )
        assert response.status_code == status.HTTP_200_OK

        new_is_active = json.loads(response.content.decode('utf-8')).get("is_active", None)
        assert update_user.is_active == new_is_active

    def test_delete_user_api(self):
        del_user = get_user_model().objects.last()
        response = self.client.delete(reverse("api:user-detail", args=[del_user.pk]))

        assert response.status_code == status.HTTP_204_NO_CONTENT

