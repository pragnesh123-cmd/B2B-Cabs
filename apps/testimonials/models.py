from django.db import models
from apps.common.models import TimeStampedModel

# Create your models here.
class Testimonials(TimeStampedModel):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(unique=True)
    testimonials = models.TextField()
    status = models.BooleanField(default=True)
    is_confirm = models.BooleanField(default=False)