from django.urls import path
from django.conf.urls import url
from .member import urlpatterns as member_urls
from .minute import urlpatterns as minute_urls
from .notification import urlpatterns as notification_urls


urlpatterns = [] + member_urls + minute_urls + notification_urls
