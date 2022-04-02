from rest_framework import serializers
from apps.accounts.models import User

class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "phone_number",
            "razorpay_account_id",
            "state",
            "city",
        )


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
