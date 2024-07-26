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

from .serializers import UserCreateSerializer, UserListSerializer, UserLoginSerializer, UserRefreshSerializer


class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListSerializer
    queryset = get_user_model().objects.all()


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

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


class PasswordResetView(APIView):
    pass


class PasswordResetConfirmView(APIView):
    pass


class FacebookSignInView(APIView):
    pass


class GoogleSignInView(APIView):
    pass
