from rest_framework.routers import SimpleRouter
from ..views.minute import MinuteAPI

router = SimpleRouter()

router.register("minute", MinuteAPI, basename="minute")

urlpatterns = [] + router.urls
