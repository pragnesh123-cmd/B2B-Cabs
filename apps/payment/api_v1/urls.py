from django.urls import re_path
from rest_framework import routers
from apps.accounts.api_v1 import views

router = routers.SimpleRouter()
# router.register("payment", views.PaymentViewSet)

app_name = "payment"

urlpatterns = [
    # re_path(r"social-registration/", views.SocialSignupAPIView.as_view()),
] + router.urls
