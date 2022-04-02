from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from apps.accounts.models import User
from apps.accounts.api_v1.serializers import UserReadSerializer,UserCreateSerializer
from django.contrib.auth.hashers import check_password,make_password



class VendorRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        password = make_password(self.request.data.pop("password"))
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )


class VendorViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    pagination_class = None
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserReadSerializer
        return UserCreateSerializer

    def get_queryset(self):
        queryset = super(VendorViewSet, self).get_queryset()
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        password = make_password(self.request.data.pop("password"))
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(password=password)
        return Response(UserReadSerializer(instance).data, status=status.HTTP_200_OK)


class LoginVerifyAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        data = {}
        user = User.objects.filter(email=email).first()
        if user:
            if check_password(password,user.password):
                data['msg'] = 'User successfully Login'
                data['valid'] = True
                data['token']=Token.objects.get(user=user).key
            else:    
                data['response'] = 'You have entered an invalid password'
                data['valid'] = False
        else:
            data['response'] = 'You have entered an invalid email'
            data['valid'] = False     
        return Response(data)
    

