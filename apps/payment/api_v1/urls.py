from django.urls import re_path
from rest_framework import routers
from apps.payment.api_v1 import views

router = routers.SimpleRouter()
# router.register("paymentconfirm", views.PaymentConfirmViewSet)

app_name = "payment"

urlpatterns = [
    re_path(r"payment-link-create", views.PaymentLinkCreateAPIView.as_view()),
    re_path(r"create-razorpay-account", views.CreateRazorpayAcoountAPIView.as_view()),
    re_path(r"payment-confirm", views.PaymentConfirmAPIView.as_view()),
] + router.urls
