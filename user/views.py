from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from time import time
from .forms import SignUpForm

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
            return redirect('https://httpbin.org/')
    else:
        form = SignUpForm()
    return render(request, 'user/sign_up.html', {'form': form})

#test
