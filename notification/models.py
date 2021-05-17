from django.db import models

from club.models import BranchClub
from ums.models import User


class BaseModel(models.Model):
    club = models.ForeignKey(BranchClub, blank=True, null=True, on_delete=models.CASCADE)
    action_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notification(BaseModel):
    title = models.CharField(max_length=255, default=None)
    message = models.TextField()
