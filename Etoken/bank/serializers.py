from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields='__all__'
    

class BankTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bank_Token
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields=('id','username','password')

    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if user and user.is_active:
            return {'user':user}
        raise serializers.ValidationError("Incorrect Credentials")
