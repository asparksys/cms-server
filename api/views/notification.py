from rest_framework.viewsets import ModelViewSet

from ..serializers.notification import NotificationSerializer
from notification.models import Notification


class NotificationAPI(ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):

        queryset = self.queryset.filter(club=self.request.user.club_id)
        return queryset
