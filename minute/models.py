from django.db import models
from ums.models import User
from club.models import  BranchClub

class BaseModel():
    club = models.ForeignKey(BranchClub, on_delete=models.CASCADE)
    action_by = models.ForeignKey(User, on_delete=models.CASCADE) 

class Agenda(BaseModel,models.Model):
    agenda = models.CharField(max_length=255,blank=False,default=None,null=False)

    def __str__(self):
        return self.agenda

class Minute(BaseModel,models.Model):
    date = models.DateTimeField(auto_now_add=True)
    minute = models.TextField(blank=False,null=False, default=None)
    agenda = models.ManyToManyField(Agenda)
    attendes = models.CharField(max_length=255)

    def __str__(self):
        return self.date



