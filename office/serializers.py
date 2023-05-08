from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
    
class OfficeTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Office_Token
        fields='__all__'