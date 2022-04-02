from django.db import models
from apps.common.models import TimeStampedModel
# Create your models here.
class Subscribers(TimeStampedModel):
    email = models.EmailField(unique=True)