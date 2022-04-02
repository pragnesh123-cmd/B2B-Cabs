from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from apps.contactus.models import ContactUs
from apps.contactus.api_v1.serializers import ContactUsSerializer
from rest_framework.permissions import AllowAny


class ContactusViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = ContactUs.objects.all()

    def get_serializer_class(self):
        return ContactUsSerializer

    def get_queryset(self):
        queryset = super(ContactusViewSet, self).get_queryset()
        return queryset

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )   