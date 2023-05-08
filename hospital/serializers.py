from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *



    
class HospitalTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hospital_Token
        fields='__all__'