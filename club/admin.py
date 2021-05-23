from django.contrib import admin

from .models import BranchClub
from .models import HeadClub

admin.site.register([HeadClub, BranchClub])
admin.site.site_header = "Club Management System: Asparksys"
