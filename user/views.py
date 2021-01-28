from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from time import time

from .forms import SignUpForm, SetupProfileForm
from .models import ProfileUser

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = "user{}".format(str(round(time())))
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            User.objects.create_user(username=username, password=password1, email=email)
            user = authenticate(username=username, password=password1)
            login(request, user)
            return HttpResponseRedirect('/setup/')
    else:
        form = SignUpForm()
    return render(request, 'user/sign_up.html', {'form': form})

@login_required()
def setup_profile(request):
    if request.method == 'POST':
        form = SetupProfileForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return HttpResponseRedirect('/profile/')
    else:
        form = SetupProfileForm()
    return render(request, 'user/profile_setup.html', {'form':form})

def user_profile(request):
    user = ProfileUser.objects.get(user=request.user)
    return render(request, 'user/user_profile.html', {'user':user})
