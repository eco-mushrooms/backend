import jwt
from typing import Any, Dict
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .utils import generate_access_token, generate_refresh_token
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from core.authenticate import JWTAuthentication


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'username',
                  'last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role', 'regular')

        user = User.objects.create_user(**validated_data, role=role)

        if role == 'regular':
            user.is_staff = True
            user.save()

        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'role']
        read_only_fields = ['id', 'email',
                            'first_name', 'last_name', 'role']


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs: Dict[str, Any]) -> Dict[Any, Any]:
        authentication_kwargs = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        try:
            authentication_kwargs['request'] = self.context.get('request')
        except Exception as e:
            pass

        self.user = authenticate(**authentication_kwargs)

        if self.user is None:
            raise AuthenticationFailed('User with given credentials not found')

        data = {
            'access': generate_access_token(self.user),
            'refresh': generate_refresh_token(self.user)
        }

        return data


class UserRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)

    def validate(self, attrs: Dict[str, Any]) -> Dict[Any, Any]:
        refresh = attrs.get('refresh')

        if refresh is None:
            raise ValidationError('Refresh token is required')

        user = JWTAuthentication.authenticate_credentials(refresh)[0]

        data = {
            'access': generate_access_token(user)
        }
