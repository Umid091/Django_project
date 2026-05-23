from django.urls import path
from .views import RegisterAPIView, LoginAPIView, RefreshTokenAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user_register'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='user_token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='user_logout'),
]