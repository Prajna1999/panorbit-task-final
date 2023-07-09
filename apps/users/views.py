from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User
from .utils import generate_otp

from django.contrib.auth import login
# Create your views here.
def login_request(request):
    return HttpResponse("Hello from login page")
    # if request.method=="POST":
    #     email=request.POST['email']
    #     user=User.objects.filter(email=email).first()

    #     if user is None:
    #         messages.error(request, 'User does not exist')
    #         return redirect('login')
    #     otp=generate_otp()
    #     send_mail(
    #         'Your OTP',
    #         'Your OTP for login is '+str(otp),
    #         'from@example.com',
    #         [email],
    #         fail_silently=False,
    #     )

    #     request.session['otp']=otp
    #     request.session['email']=email
    #     return redirect('validate_otp')



def validate_login(request):
    if request.method=="POST":
        otp=request.POST['otp']

        if(int(otp)==request.session['otp']):
            user=User.objects.get(email=request.session['email'])
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid OTP')
        return redirect('login')
    return render(request, 'validate_otp.html')

