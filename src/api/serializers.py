
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
          'id',
          'username',
          'first_name',
          'last_name',
          'is_active',
          'last_login',
          'is_superuser'
        ]
