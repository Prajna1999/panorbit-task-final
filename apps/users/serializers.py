from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email', 'first_name', 'last_name', 'gender', 'phone_number']

class OTPSerializer(serializers.Serializer):
    otp=serializers.IntegerField()