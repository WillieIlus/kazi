from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from .views import UserListView, UserProfileView


urlpatterns = [
    path('api/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenRefreshView.as_view(), name='token_verify'),

    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<uuid:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('users/<uuid:pk>/update/', UserProfileView.as_view(), name='user_profile_update'),
    path('users/<uuid:pk>/delete/', UserProfileView.as_view(), name='user_profile_delete'),
    
]