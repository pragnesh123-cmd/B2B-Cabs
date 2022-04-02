from rest_framework import routers
from apps.contactus.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register("contactus", views.ContactusViewSet)

app_name = "contactus"

urlpatterns = [
] + router.urls
