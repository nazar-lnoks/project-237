from django.urls import path, include
from django.contrib.auth import logout
from . import views

urlpatterns = [
    path('signup/', views.signUp, name="signup_url"),
    path('login/', views.LoginView.as_view(), name="login_url"),
    path('logout/', views.logoutUser, name="logout_url"),
    path('setup/', views.setupProfile, name="setup_profile_url"),
    path('profile/', views.userProfile, name="user_profile_url"),
]