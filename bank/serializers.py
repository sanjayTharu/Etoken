from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class BankTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank_Token
        fields='__all__'

