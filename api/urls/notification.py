from rest_framework.routers import SimpleRouter

from ..views.notification import NotificationAPI

router = SimpleRouter()

router.register("notification", NotificationAPI, basename="notification")

urlpatterns = [] + router.urls
