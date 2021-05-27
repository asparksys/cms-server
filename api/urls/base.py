from django.conf.urls import url
from django.urls import path

from .member import urlpatterns as member_urls
from .minute import urlpatterns as minute_urls
from .notification import urlpatterns as notification_urls
from .user import urlpatterns as ums_urls


urlpatterns = [] + member_urls + minute_urls + notification_urls + ums_urls
