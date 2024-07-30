########################
# print("Hello World") #
########################

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserCreateSerializer, UserListSerializer, UserLoginSerializer, UserRefreshSerializer


class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        responses={status.HTTP_201_CREATED: UserCreateSerializer},
        operation_description='Create a new user')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListSerializer
    queryset = get_user_model().objects.all()

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: UserListSerializer(many=True)},
        operation_description='List all users',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        operation_description='Login a user',
        responses={status.HTTP_200_OK: openapi.Response(
            description='User login',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING),
                    'refresh': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        return Response({
            'access': user['access'],
            'refresh': user['refresh']
        }, status=status.HTTP_200_OK)


class UserRefreshView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRefreshSerializer

    @swagger_auto_schema(
        request_body=UserRefreshSerializer,
        responses={status.HTTP_200_OK: openapi.Response(
            description='User token refresh',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),)
        },
        operation_description='Refresh a user token',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PasswordResetView(APIView):
    pass


class PasswordResetConfirmView(APIView):
    pass


class FacebookSignInView(APIView):
    pass


class GoogleSignInView(APIView):
    pass
