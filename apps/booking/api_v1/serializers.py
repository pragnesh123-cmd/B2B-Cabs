from rest_framework import serializers
from apps.booking.models import PostBooking,ConfirmBooking


class PostBookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBooking
        fields = (
            "pick_up",
            "drop",
            "prefer_car",
            "cost_of_jorney",
            "commission_of_vendor",
            "date_of_jorney",
            "pickup_time",
            "customer_name",
            "customer_email",
            "customer_mobile_number"
        )


class PostBookingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBooking
        exclude = (
            "commission_of_vendor",
            "is_pickup",
        )
        depth = 1


class ConfirmBookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmBooking
        fields = (
            "driver_name",
            "driver_email",
            "driver_mobile_number",
            "driver_licence_number",
            "driver_vehicle_number"
        )

class ConfirmBookingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmBooking
        fields = "__all__"