from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.mainPage),
    path('categories/<str:slug>/', views.getCategoryCatalog, name='getCategoryCatalog_url'),
    path('products/<str:slug>/', views.getProductDetails, name='getProductDetails_url'),

    path('categories/', views.redirectToMainPage),
    path('products/', views.redirectToMainPage),
    # path('order/', views.orderPage),
    path('cart/', views.cartPage)
]
