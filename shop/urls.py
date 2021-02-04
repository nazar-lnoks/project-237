from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.mainPage, name="main_page_url"),
    path('categories/<str:slug>/', views.getCategoryCatalog, name='getCategoryCatalog_url'),
    path('products/<str:slug>/', views.getProductDetails, name='getProductDetails_url'),
    path('products/<str:slug>', views.addToCart, name='addProductToCart_url'),

    path('products/deleteFeedback/<int:id>/<str:slug>/', views.adminDeleteComment, name='adminDeleteComment_url'),
    path('search/<str:query>', views.getWantedProducts, name='getWantedproducts_url'),

    path('categories/', views.redirectToMainPage),
    path('products/', views.redirectToMainPage),
    path('order-product/<str:slug>/', views.getOrderProduct, name='orderProduct_url'),
    path('order-cart/', views.getOrderCart, name='orderCart_url'),
    path('cart/', views.getCart, name='getCart_url'),
]