from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.user import UserSerializer

User = get_user_model()


class UserTokenObtainView(TokenObtainPairView):
    serializer_class = UserSerializer
