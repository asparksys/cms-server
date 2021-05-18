from django.db import models

class Agenda(models.Model):
    agenda = models.CharField(max_length=255,blank=False,default=None,null=False)

class Minute(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    minute = models.TextField(blank=False,null=False, default=None)
    agenda = models.ManyToManyField(Agenda)
    attendes = models.CharField(max_length=255) #dummy TBD
    action_by = models.CharField(max_length=255,null=False,default=None,blank=False) #dummy TBD



