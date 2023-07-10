from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404

from .models import User
from .utils import generate_otp
from .serializers import SignupSerializer, OTPSerializer


# Create your views here.
# def login_request(request):
   
#     if request.method=="POST":
#         email=request.POST['email']
#         user=User.objects.filter(email=email).first()

#         if user is None:
#             messages.error(request, 'User does not exist')
#             return redirect('login')
#         otp=generate_otp()
#         send_mail(
#             'Your OTP',
#             'Your OTP for login is '+str(otp),
#             'from@example.com',
#             [email],
#             fail_silently=False,
#         )

#         request.session['otp']=otp
#         request.session['email']=email
#         return redirect('validate_otp')



# def validate_login(request):
#     if request.method=="POST":
#         otp=request.POST['otp']

#         if(int(otp)==request.session['otp']):
#             user=User.objects.get(email=request.session['email'])
#             login(request, user)
#             return redirect('dashboard')
#         messages.error(request, 'Invalid OTP')
#         return redirect('login')
#     return render(request, 'validate_otp.html')

@api_view(['POST'])
def signup(request):
    serializer=SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'User created successfully'
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    email=request.data.get('email')
    user=get_object_or_404(User, email=email)
    otp=generate_otp()
    send_mail(
        'Your OTP',
        'Your OTP for  login is '+str(otp),
        'gituprajna20@gmail.com',
        [user.email],
        fail_silently=False,
    )
    request.session['otp']=otp
    request.session['email']=user.email
    return Response({
        'message':'OTP sent to email'
    })
@api_view(['POST'])
def validate_otp_view(request):
    serializer=OTPSerializer(data=request.data)
    if serializer.is_valid():
        otp=serializer.validated_data['otp']
        if otp == request.session.get('otp'):
            user=get_object_or_404(User, email=request.session['email'])
            login(request,user)
            return Response({'message':'Logged in successfully'})
        return Response({'message':'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message':'Logged out successfully.'})

