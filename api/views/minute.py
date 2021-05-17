from django.db.models import query
from rest_framework.viewsets import ModelViewSet

from ..serializers.minute import MinuteSerializer
from minute.models import Minute


class MinuteAPI(ModelViewSet):
    serializer_class = MinuteSerializer
    queryset = Minute.objects.all().order_by("date_created")

    def get_queryset(self):
        queryset = self.queryset.filter(club=self.request.user.club_id)

        return queryset
