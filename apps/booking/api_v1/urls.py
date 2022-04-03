from django.urls import re_path
from rest_framework import routers
from apps.booking.api_v1 import views

router = routers.SimpleRouter()
router.register("postbooking", views.PostBookingViewSet)
router.register("confirmbooking", views.ConfirmBookingViewSet)

app_name = "booking"

urlpatterns = [
    re_path(r"pickup-action/(?P<pk>[0-9]+)/$", views.PickupActionAPIView.as_view()),
] + router.urls
