from rest_framework import generics,status,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .models import Citizen,Office_Token
from .serializers import CitizenSerializer,OfficeTokenSerializer,UserSerializer,LoginSerializer

# Create your views here.


class CitizenViewSet(viewsets.ModelViewSet):
    queryset=Citizen.objects.all()
    serializer_class=CitizenSerializer
    permission_classes=[permissions.IsAuthenticated]

class OfficeTokenViewSet(viewsets.ModelViewSet):
    queryset=Office_Token.objects.all()
    serializer_class=OfficeTokenSerializer
    permission_classes=[permissions.IsAuthenticated]

class OfficeTokenListView(generics.ListCreateAPIView):
    queryset=Office_Token.objects.all()
    serializer_class=OfficeTokenSerializer
    permission_classes=[permissions.IsAuthenticated]

class HospitalTokenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Office_Token.objects.all()
    serializer_class=OfficeTokenSerializer
    permission_classes=[permissions.IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        },status=status.HTTP_200_OK)