from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [

    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-token'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    path('change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),

    path('profile/',views.ProfileAPIView.as_view(),name='profile'),
]