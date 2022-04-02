from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from rest_framework import generics, status
from apps.booking.models import PostBooking,ConfirmBooking
from apps.booking.api_v1.serializers import PostBookingCreateSerializer,PostBookingReadSerializer,ConfirmBookingReadSerializer,ConfirmBookingWriteSerializer



class PostBookingViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    pagination_class = None
    queryset = PostBooking.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return PostBookingReadSerializer
        return PostBookingCreateSerializer

    def get_queryset(self):
        queryset = super(PostBookingViewSet, self).get_queryset()
        return queryset

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(vendor_id=request.user.id)
        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )    

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(PostBookingReadSerializer(instance).data, status=status.HTTP_200_OK)


class ConfirmBookingViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    pagination_class = None
    queryset = PostBooking.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ConfirmBookingReadSerializer
        return ConfirmBookingWriteSerializer

    def get_queryset(self):
        queryset = super(ConfirmBookingViewSet, self).get_queryset()
        return queryset

    def create(self,request,*args,**kwargs):
        postbooking_id = self.request.data.pop("postbooking_id")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(vendor_id=request.user.id,postbooking_id=postbooking_id)
        print(serializer.data)
        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )    

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(PostBookingReadSerializer(instance).data, status=status.HTTP_200_OK)    