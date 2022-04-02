from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=100, blank=True)
    last_name = models.CharField(_("last name/surname"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(_("password"), max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # is_verified = models.BooleanField(default=False)
    # privacy_and_GTC = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]