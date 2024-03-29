from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.views import View
from time import time

from .forms import SignUpForm, SetupProfileForm, LogInForm
from .models import ProfileUser
from shop.models import *

def genCartContext(request):
    orders_cart = CartProduct.objects.filter(user=request.user)
    amount_cart = len(orders_cart)

    orders = Order.objects.filter(user=request.user)
    objects_cart = []

    for i in orders_cart:
        model = i.contentType.model_class()
        product = model.objects.get(id=i.objectId)

        order = {
            'product': product
        }
        objects_cart.append(order)
    
    context={
        'orders':objects_order,
        'amount_cart': amount_cart,
        'products_cart':objects_cart
    }

    return context

def signUp(request):
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
                return HttpResponseRedirect('/')
        return render(request, 'user/login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def setupProfile(request):
    if request.method == 'POST':
        form = SetupProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return HttpResponseRedirect('/')
    else:
        form = SetupProfileForm()
    return render(request, 'user/profile_setup.html', {'form':form})

@login_required()
def userProfile(request):
    user = request.user
    account = get_object_or_404(ProfileUser, user=user)

    if request.method == "POST":
        form = SetupProfileForm(data=request.POST, files=request.FILES, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/account/profile')
    else:
        form = SetupProfileForm(instance=account)
        

    orders_cart = CartProduct.objects.filter(user=request.user)

    amount_cart = 0
    totalPrice = 0
    for i in orders_cart:
        amount_cart += i.count
        totalPrice += i.price

    context = {
        'form':form, 
        'user':account,
        'amount_cart': amount_cart,
        'products_cart':orders_cart,
        'totalPrice': totalPrice
    }
    return render(request, 'user/user_profile.html', context)

@login_required()
def orderHistory(request):
    account = get_object_or_404(ProfileUser, user=request.user)
    orders = Order.objects.filter(user=request.user)

    orders_cart = CartProduct.objects.filter(user=request.user)
    
    objects_order = []
    objects_cart = []

    amount_cart = 0
    totalPrice = 0
    for i in orders_cart:
        amount_cart += i.count
        totalPrice += i.price

    print(amount_cart)
    
    for p in orders:
        model = p.contentType.model_class()

        try:
            product = model.objects.get(id=p.objectId)
        except model.DoesNotExist:
            pass
        else:
            order = {
                'date': p.date_delivery,
                'product': product
            }
            objects_order.append(order)

    print(objects_order)
    context={
        'user':account, 
        'orders':objects_order,
        'amount_cart': amount_cart,
        'products_cart':orders_cart,
        'totalPrice': totalPrice
    }
    return render(request, 'user/order_history.html', context)