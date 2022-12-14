from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.registration import RegistrationView
from .views.test_view import TestView


app_name = "users"


urlpatterns = [
    path('register', RegistrationView.as_view()),
    path('test', TestView.as_view()),

    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]