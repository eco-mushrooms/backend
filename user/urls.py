from django.urls import path, re_path
from .views import CreateUserView, PasswordResetConfirmView, PasswordResetView, UserListView, UserLoginView, UserRefreshView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('create/', CreateUserView.as_view(), name='register'),
    path('refresh/', UserRefreshView.as_view(), name='refresh'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(
    ), name='password-reset-confirm'),

]
