from rest_framework import routers
from apps.accounts.api_v1 import views
from django.urls import re_path

router = routers.SimpleRouter()
router.register("vendors", views.VendorViewSet)

app_name = "accounts"

urlpatterns = [
    re_path(r"login-verify/", views.LoginVerifyAPIView.as_view()),
    re_path(r"vendor-registration/", views.VendorRegistrationAPIView.as_view()),
] + router.urls
