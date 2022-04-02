from django.contrib import admin
from apps.booking.models import PostBooking,ConfirmBooking

# Register your models here.
admin.site.register(PostBooking)
admin.site.register(ConfirmBooking)