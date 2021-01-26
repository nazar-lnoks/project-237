from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.mainPage),
    path('categories/', views.redirectToMainPage),
    path('products/', views.redirectToMainPage),
    path('categories/<str:slug>', views.categoryPage),
    path('products/<str:slug>', views.productPage),
    path('order/', views.orderPage),
    path('cart/', views.cartPage)
]
