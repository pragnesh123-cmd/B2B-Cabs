from rest_framework import routers
from apps.subscribers.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register("subscribers", views.SubscribersViewSet)

app_name = "subscribers"

urlpatterns = [
] + router.urls
