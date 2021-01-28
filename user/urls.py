from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup_url"),
    path('setup/', views.setup_profile, name="setup_profile_url"),
    path('profile/', views.user_profile, name="user_profile_url")
]