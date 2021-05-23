from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
