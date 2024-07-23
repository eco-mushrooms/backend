from django.urls import path
from .views import CreateUserView, UserListView, UserLoginView, UserRefreshView

urlpatterns = [
    path('/', UserListView.as_view(), name='users'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('create/', CreateUserView.as_view(), name='register'),
    path('refresh/', UserRefreshView.as_view(), name='refresh'),
]
