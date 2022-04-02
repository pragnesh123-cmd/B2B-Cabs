from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from apps.testimonials.models import Testimonials
from apps.testimonials.api_v1.serializers import TestimonialsSerializer
from rest_framework.permissions import AllowAny


class TestimonialsViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = Testimonials.objects.all()

    def get_serializer_class(self):
        return TestimonialsSerializer

    def get_queryset(self):
        queryset = super(TestimonialsViewSet, self).get_queryset()
        return queryset

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )   