from rest_framework import routers
from apps.manage_pages.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
# router.register("subscribers", views.SubscribersViewSet)

app_name = "manage_pages"

urlpatterns = [
] + router.urls
