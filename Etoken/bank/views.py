from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render
from .models import Customer,Bank_Token
from .serializers import CustomerSerializer,BankTokenSerializer,UserSerializer,LoginSerializer

# Create your views here.

class BankTokenList(generics.ListCreateAPIView):
    queryset=Bank_Token.objects.all()
    serializer_class=BankTokenSerializer
    permission_classes=[permissions.IsAuthenticated]

class BankTokenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bank_Token.objects.all()
    serializer_class=BankTokenSerializer
    permission_classes=[permissions.IsAuthenticated]


class UserRegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class= LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        },status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[permissions.IsAuthenticated]


class BankTokenViewSet(viewsets.ModelViewSet):
    queryset=Bank_Token.objects.all()
    serializer_class=BankTokenSerializer
    permission_classes=[permissions.IsAuthenticated]