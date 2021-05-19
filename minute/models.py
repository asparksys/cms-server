from django.db import models
from ums.models import User
from club.models import  BranchClub
from member.models import Member

class BaseModel(models.Model):
    club = models.ForeignKey(BranchClub, blank=True,null=True, on_delete=models.CASCADE)
    action_by = models.ForeignKey(User,blank=True,null=True,  on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Minute(BaseModel):
    minute = models.TextField(blank=True,null=True, default=None)
    agenda = models.TextField(default=None)
    attendes = models.ManyToManyField(Member)

    def __str__(self):
        return self.date



