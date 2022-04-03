from rest_framework import routers
from apps.testimonials.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register("testimonials", views.TestimonialsViewSet)

app_name = "testimonials"

urlpatterns = [
    re_path(r"testimonials-confirm-action/(?P<pk>[0-9]+)/$", views.TestimonialsConfirmActionAPIView.as_view()),
    re_path(r"testimonials-status-action/(?P<pk>[0-9]+)/$", views.TestimonialsStatusActionAPIView.as_view()),
] + router.urls
