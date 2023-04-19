from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username','password','email')
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        user=User.objects.create_user(
            validated_data['username'],validated_data['email'],validated_data['password'])
        return user
    

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        user=authenticate(username=data['username'],password=data['password'])
        if user and user.is_active:
            return {'user':user}
        raise serializers.ValidationError("Incorrect Credentials")
    


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'

    
class HospitalTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hospital_Token
        fields='__all__'