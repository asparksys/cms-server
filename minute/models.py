from django.db import models
from ums.models import User
from club.models import  BranchClub
from member.models import Member

class BaseModel():
    club = models.ForeignKey(BranchClub, blank=True,null=True, on_delete=models.CASCADE)
    action_by = models.ForeignKey(User,blank=True,null=True,  on_delete=models.CASCADE) 

class Agenda(BaseModel,models.Model):
    agenda = models.CharField(max_length=255,blank=True,default=None,null=True)

    def __str__(self):
        return self.agenda

class Minute(BaseModel,models.Model):
    date = models.DateTimeField(auto_now_add=True)
    minute = models.TextField(blank=True,null=True, default=None)
    agenda = models.ManyToManyField(Agenda)
    attendes = models.ManyToManyField(Member)

    def __str__(self):
        return self.date



