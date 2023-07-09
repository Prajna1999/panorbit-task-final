# panorbit-task-final-main/apps/users/urls.py

from django.urls import path
from .views import login_request, validate_login

urlpatterns = [
    path('login/', login_request, name='login'),
    path('validate_otp/', validate_login, name='validate_otp'),
]
