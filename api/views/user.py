from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from ..serializers.user import UserSerializer

User = get_user_model()


class UserTokemObtainView(TokenObtainPairView):
    serializer_class = UserSerializer
