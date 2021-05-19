from django.urls import path
from django.conf.urls import url
from .member import urlpatterns as member_urls


urlpatterns = [] + member_urls
