from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from django.urls import path
from .views import *

urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]