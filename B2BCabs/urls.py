"""B2BCabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

api_v1_urls = [
    re_path("accounts/", include("apps.accounts.api_v1.urls", namespace="v1-account")),
    re_path("booking/", include("apps.booking.api_v1.urls", namespace="v1-booking")),
    re_path("payment/", include("apps.payment.api_v1.urls", namespace="v1-payment")),
    re_path("contactus/", include("apps.contactus.api_v1.urls", namespace="v1-contactus")),
    re_path("subscribers/", include("apps.subscribers.api_v1.urls", namespace="v1-subscribers")),
    re_path("testimonials/", include("apps.testimonials.api_v1.urls", namespace="v1-testimonials")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(api_v1_urls)),
]
