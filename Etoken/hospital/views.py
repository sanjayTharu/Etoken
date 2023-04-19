from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Patient,Hospital_Token
from .serializers import PatientSerializer,HospitalTokenSerializer,LoginSerializer,UserSerializer
# Create your views here.

class HospitalTokenListView(generics.ListCreateAPIView):
    queryset=Hospital_Token.objects.all()
    serializer_class=HospitalTokenSerializer
    permission_classes=[permissions.IsAuthenticated]

class HospitalTokenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=HospitalTokenSerializer
    pagination_class=[permissions.IsAuthenticated]

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
            'access': str(refresh.access_token),
        },status=status.HTTP_200_OK)




class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    permission_classes=[permissions.IsAuthenticated]

class HospitalTokenViewSet(viewsets.ModelViewSet):
    queryset=Hospital_Token.objects.all()
    serializer_class=HospitalTokenSerializer
    permission_classes=[permissions.IsAuthenticated]