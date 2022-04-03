from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,generics
from apps.testimonials.models import Testimonials
from apps.testimonials.api_v1.serializers import TestimonialsSerializer,TestimonialsConfirmActionSerializer,TestimonialsStatusActionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication


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

class TestimonialsConfirmActionAPIView(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsConfirmActionSerializer
   
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)         

class TestimonialsStatusActionAPIView(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsStatusActionSerializer
   
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)           