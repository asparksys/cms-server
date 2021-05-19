from django.contrib import admin
from .models import HeadClub, BranchClub

admin.site.register([HeadClub, BranchClub])
admin.site.site_header = "Club Management System: Asparksys"
