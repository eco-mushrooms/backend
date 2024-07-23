from django.urls import path
from .views import CreateUserView, UserListView, UserLoginView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('login/', UserLoginView.as_view(), name='login'),
]
