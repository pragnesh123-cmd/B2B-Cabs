from rest_framework import serializers
from apps.testimonials.models import Testimonials


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"


class TestimonialsConfirmActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ("is_confirm",)  

class TestimonialsStatusActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ("status",)  
