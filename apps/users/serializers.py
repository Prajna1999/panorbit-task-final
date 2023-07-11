from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[ 'first_name', 'last_name', 'gender','email' ,'phone_number']

class OTPSerializer(serializers.Serializer):
    otp=serializers.IntegerField()