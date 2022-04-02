from rest_framework import serializers
from apps.testimonials.models import Testimonials


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"
