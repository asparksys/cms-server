from django.contrib import admin
from .models import MemberRole, Member

admin.site.register([MemberRole,Member])
