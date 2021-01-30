from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.views import View
from time import time

from .forms import SignUpForm, SetupProfileForm, LogInForm
from .models import ProfileUser

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            username = email.lower()
            
            User.objects.create_user(username=username, password=password1, email=email)
            user = authenticate(username=username, password=password1)
            login(request, user)
            return HttpResponseRedirect('/account/setup')
    else:
        form = SignUpForm()
    return render(request, 'user/sign_up.html', {'form': form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(request, 'user/login.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = LogInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/account/profile')
            else:
                print(messages.error(request,'username or password not correct'))
                # return HttpResponseRedirect('/account/login')
        return render(request, 'user/login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def setup_profile(request):
    if request.method == 'POST':
        form = SetupProfileForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return HttpResponseRedirect('/account/profile')
    else:
        form = SetupProfileForm()
    return render(request, 'user/profile_setup.html', {'form':form})

def user_profile(request):
    if request.user:
        user = ProfileUser.objects.get(user=request.user)
    else:
        user = None
    return render(request, 'user/user_profile.html', {'user':user})
