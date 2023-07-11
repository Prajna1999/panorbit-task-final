# panorbit-task-final-main/apps/users/urls.py

from django.urls import path
from .views import signup, login_view, validate_otp_view, logout_view,search_view, search_results

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('validate_otp/', validate_otp_view, name='validate_otp'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_view, name='search'),
    path('search/results/',search_results, name="search_results")
    
]
