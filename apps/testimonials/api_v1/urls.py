from rest_framework import routers
from apps.testimonials.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register("testimonials", views.TestimonialsViewSet)

app_name = "testimonials"

urlpatterns = [
] + router.urls
