from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from apps.subscribers.models import Subscribers
from apps.subscribers.api_v1.serializers import SubscribersSerializer
from rest_framework.permissions import AllowAny


class SubscribersViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = Subscribers.objects.all()

    def get_serializer_class(self):
        return SubscribersSerializer

    def get_queryset(self):
        queryset = super(SubscribersViewSet, self).get_queryset()
        return queryset

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )   