from django.urls import path
from rest_framework.routers import SimpleRouter
from ..views.member import MemberRoleAPI

router = SimpleRouter()

router.register(
    "member-role",
    MemberRoleAPI,
    basename="member-role",
)

urlpatterns = [] + router.urls
