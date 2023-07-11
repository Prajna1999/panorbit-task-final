from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Country
from .utils import generate_otp
from .serializers import SignupSerializer, OTPSerializer

from django.http import JsonResponse
from django.db.models import Q

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'message': 'User created successfully'})
            except TypeError:
                return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'signup.html')

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        otp = generate_otp()
        send_mail(
            'Your OTP',
            'Your OTP for  login is ' + str(otp),
            'gituprajna20@gmail.com',
            [user.email],
            fail_silently=False,
        )
        request.session['otp'] = otp
        request.session['email'] = user.email
        return redirect('validate_otp')
    return render(request, 'login.html')

@api_view(['GET', 'POST'])
def validate_otp_view(request):
    if request.method == 'POST':
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data['otp']
            if otp == request.session.get('otp'):
                user = get_object_or_404(User, email=request.session['email'])
                login(request, user)
                # return Response({'message': 'Logged in successfully'})
                return redirect('search')
            return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'validate_otp.html')

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def search_view(request):
    return render(request, 'search.html')
@login_required
def search_results(request):
    query = request.GET.get('q', '')
    results = User.objects.filter(name__icontains=query)
    context = {'results': results, 'query': query}
    return render(request, 'search_results.html', context)
