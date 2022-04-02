from django.db import models
from apps.common.models import TimeStampedModel


# Create your models here.

class PostBooking(TimeStampedModel):
    vendor = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    pick_up = models.CharField(max_length=500,blank=True,null=True)
    drop = models.CharField(max_length=500,blank=True,null=True)
    prefer_car = models.CharField(max_length=100,blank=True,null=True)
    cost_of_jorney = models.IntegerField(blank=True,null=True)
    commission_of_vendor = models.IntegerField(blank=True,null=True)
    date_of_jorney = models.DateField()
    pickup_time = models.TimeField()
    is_pickup = models.BooleanField(default=False)
    state = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    
    customer_name = models.CharField(max_length=500,blank=True,null=True)
    customer_email = models.CharField(max_length=500,blank=True,null=True)
    customer_mobile_number = models.CharField(max_length=500,blank=True,null=True)


class ConfirmBooking(TimeStampedModel):
    vendor = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    postbooking = models.ForeignKey("booking.PostBooking",on_delete=models.CASCADE)
    is_booking_confirm = models.BooleanField(default=False)

    # razorpay_plink_id = models.CharField(max_length=100,blank=True,null=True)
    # razorpay_pay_id = models.CharField(max_length=100,blank=True,null=True)
    # razorpay_plink_id = models.CharField(max_length=100,blank=True,null=True)

    driver_name = models.CharField(max_length=500,blank=True,null=True)
    driver_email = models.CharField(max_length=500,blank=True,null=True)
    driver_mobile_number = models.CharField(max_length=500,blank=True,null=True)
    driver_licence_number = models.CharField(max_length=500,blank=True,null=True)
    driver_vehicle_number = models.CharField(max_length=500,blank=True,null=True)