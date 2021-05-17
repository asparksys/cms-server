from django.contrib import admin

from .models import Member
from .models import MemberRole

admin.site.register([MemberRole, Member])
