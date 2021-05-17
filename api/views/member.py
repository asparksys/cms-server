from rest_framework.viewsets import ModelViewSet
from member.models import MemberRole
from ..serializers.member import MemberRoleSerializer


class MemberRoleAPI(ModelViewSet):
    serializer_class = MemberRoleSerializer
    queryset = MemberRole.objects.all().order_by("name")

    def get_queryset(self):

        queryset = self.queryset.filter(club_id=self.request.user.club_id)
        return queryset
