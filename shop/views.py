from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from . import models

from django.apps import apps


def redirectToMainPage(request):
    return redirect('/')

# def get_subclasses(abstract_class):
#    result = []
#    for model in apps.get_app_config('shop').get_models():
#       if issubclass(model, abstract_class) and model is not abstract_class:
#            result.append(model)
#    return result

def getProductBySlug(slug):

    products = []
    for model in apps.get_app_config('shop').get_models():
       if issubclass(model, models.Product) and model is not models.Product:
           products.append(model)

    result = []

    for product in products:
        qs = product.objects.filter(slug=slug)
        if len(qs)>0: result.append( qs )
    
    if len(result) > 0:
        return result[0][0]

    return None


def mainPage(request):

    categories = models.Category.objects.all()

    return render(request, 'shop/main_page.html', context={'categories':categories})

def getCategoryCatalog(request, slug):

    try:
        category_ = models.Category.objects.get(slug__iexact=slug)

        products = []
        for model in apps.get_app_config('shop').get_models():
            if issubclass(model, models.Product) and model is not models.Product:
                products.append(model)

        result = []

        for product in products:
            qs = product.objects.filter(category=category_.id)
            if len(qs)>0: result.append( qs )


        context = {'category':category_, 'qs_products': result}

    except models.Category.DoesNotExist: 
        return redirectToMainPage(request)
    
    return render(request, 'shop/category_page.html', context)

def getProductDetails(request, slug):
    
    product = getProductBySlug(slug)

    if product != None:

        context = { 'product':product }

        return render(request, 'shop/product_page.html', context)

    return redirectToMainPage(request)

# def addToCart(slug):
    

#     product = getProductBySlug(slug)

#     contentType = product.id
#     objectId = product.id
#     contentObject = product


#     newCart = CartProduct.objects.create(user=,contentType=contentType,objectId=objectId,contentObject=contentObject)

def cartPage(request):

    # newCart = CartProduct.objects.create(user=,contentType=,objectId=)
    return HttpResponse("Cart page")