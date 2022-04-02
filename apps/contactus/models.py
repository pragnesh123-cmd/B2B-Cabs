from django.db import models
from apps.common.models import TimeStampedModel

# Create your models here.
class ContactUs(TimeStampedModel):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    msg = models.TextField()