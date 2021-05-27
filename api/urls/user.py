from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from ..views.user import UserTokenObtainView

urlpatterns = [
    path("token/", UserTokenObtainView.as_view(), name="user-token-obtain-view"),
    path("token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
]
