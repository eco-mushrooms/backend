import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import ValidationError, AuthenticationFailed

User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        auth_token = auth_header.split(" ")

        if len(auth_token) != 2:
            raise ValidationError(
                "Auth token must be of the form 'Bearer <token>'")

        token = auth_token[1]

        return self.authenticate_credentials(token)

    @classmethod
    def authenticate_credentials(cls, token):
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Access token expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

        user = User.objects.get(id=payload['user_id'])

        return (user, token)
