from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields='__all__'

    
class OfficeTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office_Token
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username','password','email')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User.objects.create_user(
            validated_data['username'],validated_data['email'],validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        user=authenticate(username=data['username'],password=data['password'])
        if user and user.is_active:
            return {'user':user}
        raise serializers.ValidationError("Incorrect Credentials")

