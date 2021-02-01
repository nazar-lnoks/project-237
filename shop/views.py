from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType
from .forms import OrderForm
from . import models

from user.models import ProfileUser

from django.apps import apps


DEBUG = 1


# redirect to main page
def redirectToMainPage(request):
    return redirect('/')


# return one product with specified slug
# returns None if there is no product with specified slug 
def getProductBySlug(slug):
    # get all products of specified type from app('shop')
    products = []
    for model in apps.get_app_config('shop').get_models():
       if issubclass(model, models.Product) and model is not models.Product:
           products.append(model)

    # get products with specified slug
    result = []
    for product in products:
        qs = product.objects.filter(slug=slug)
        if len(qs)>0: result.append(qs)
    
    if DEBUG: print("getProductBySlug(slug: {}) return: ".format(slug), end='')

    # return the first only product from first QuerySet if exists
    if len(result) > 0:
        if DEBUG: print(result[0][0])

        return result[0][0]

    if DEBUG: print("None")

    return None


# return product QuerySet
def getCartProductsByUserId(id):
    # get user object by id
    user = models.User.objects.get(id=id)

    # get all cart products which belong to user
    products = models.CartProduct.objects.filter(user=user)

    if DEBUG: print("getCartProductsByUserId(id: {}) return: ".format(id), end='')

    # return one product QuerySet if exists
    if len(products) > 0:
        if DEBUG: print(products)

        return products

    if DEBUG: print("None")

    return None

def mainPage(request):

    topProducts = getTopProducts()
    categories = models.Category.objects.all()

    empty = False
    if len(categories) == 0:
        empty = True
    
    if request.user.is_anonymous:
        context={'categories':categories, 'empty':empty, 'topProducts':topProducts}
    else:
        account = get_object_or_404(ProfileUser, user=request.user)
        context={'categories':categories, 'empty':empty, 'topProducts':topProducts, 'account':account}

    return render(request, 'shop/main_page.html', context)

# render catalog for specified category 
def getCategoryCatalog(request, slug):
    try:
        # get category with specified slug
        category_ = models.Category.objects.get(slug__iexact=slug)

        # get all products of specified type from app('shop')
        products = []
        for model in apps.get_app_config('shop').get_models():
            if issubclass(model, models.Product) and model is not models.Product:
                products.append(model)

        # get all products which belong to specified category
        result = []
        for product in products:
            qs = product.objects.filter(category=category_.id)
            if len(qs)>0: result.append( qs )

        context = {'category':category_, 'qs_products': result}

    except models.Category.DoesNotExist:
        if DEBUG: print("getCategoryCatalog() redirect ")

        return redirectToMainPage(request)
    
    if DEBUG: print("getCategoryCatalog() context: {}: ".format(context))

    return render(request, 'shop/category_page.html', context)


# render product page
def getProductDetails(request, slug):
    # get product with specified slug
    product = getProductBySlug(slug)

    if product != None:
        context = { 'product':product }

        if DEBUG: 
            print("getProductDetails() context: {}: ".format(context))

        return render(request, 'shop/product_page.html', context)

    if DEBUG: print("getProductDetails() return")

    return redirectToMainPage(request)


# add product with specified slug to cart
def addToCart(request, slug):
    # get product with specified slug
    product = getProductBySlug(slug)
    
    # fill ContentType foreign key
    contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
    objectId = product.id
    contentObject = product

    # get current user
    user = request.user

    if user.id == None:
        if DEBUG: print("addToCart() Anonymous user")

        return redirect('/products/{}/'.format(str(slug)))

    # create cart product object
    models.CartProduct.objects.create(user=request.user, \
                                      contentType=contentType, \
                                      objectId=objectId, \
                                      contentObject=contentObject, \
                                      price=product.price, \
                                      count=1)

    if DEBUG: print("addToCart() added")

    return redirect('/products/{}/'.format(str(slug)))


# render cart page
def getCart(request):
    # get current user 
    user = request.user

    if user.id == None:
        if DEBUG: print("getCart() user is not authorized")

        return HttpResponse('Login')

    # get cart products
    cartProducts = models.CartProduct.objects.filter(user=user)

    context = { 'cartProducts': cartProducts }

    if DEBUG: print("getCart() context: {}".format(context))

    return render(request, 'shop/cart_page.html', context)


# render order page for one product
def getOrderProduct(request, slug):
    # get current use id
    id = request.user.id
    if id == None:
        return HttpResponse("user is not authorized")

    # get product with specified slug
    product = getProductBySlug(slug)
    if product == None:
        return HttpResponse("Product not found")

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # read fields
            deliveryAddress = form.cleaned_data['deliveryAddress']
            paymentMethod = form.cleaned_data['payment']
    
            # fill ContentType foreign key
            contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
            objectId = product.id
            contentObject = product
            
            # create order object
            models.Order.objects.create(user=request.user, \
                                contentType=contentType,
                                objectId=objectId,
                                contentObject=contentObject,
                                deliveryAddress=deliveryAddress,
                                payment=paymentMethod)

            if DEBUG: print("getOrderProduct() ordered")

            return HttpResponse("Ordered")
    else:
        form = OrderForm()

    context = {'form': form, 'product': product}

    if DEBUG: print("getOrderProduct() context: {}".format(form))

    return render(request, 'shop/order_page.html', context)


# render cart order page
def getOrderCart(request):
    # get current use id
    id = request.user.id
    if id == None:
        return HttpResponse("user is not authorized")


    cartProducts = getCartProductsByUserId(id)
    if cartProducts == None:
        return HttpResponse("Product not found")

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # read fields
            deliveryAddress = form.cleaned_data['deliveryAddress']
            paymentMethod = form.cleaned_data['payment']
            
            for cartProduct in cartProducts:
                # fill ContentType foreign key
                contentType = cartProduct.contentType
                objectId = cartProduct.objectId
                contentObject = cartProduct.contentObject
                
                # create order object
                models.Order.objects.create(user=request.user, \
                                    contentType=contentType,
                                    objectId=objectId,
                                    contentObject=contentObject,
                                    deliveryAddress=deliveryAddress,
                                    payment=paymentMethod)

            for cartProduct in cartProducts:
                cartProduct.delete()

            if DEBUG: print("getOrderCart() ordered")

            return HttpResponse("Ordered")
    else:
        form = OrderForm()


    context = {'form': form, 'cartProducts': cartProducts}

    if DEBUG: print("getOrderCart() context: {} cartProducts: {}".format(form, cartProducts))

    return render(request, 'shop/ordercart_page.html', context)

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

def getProductByRate(averageRate, category):

    products = []
    for model in apps.get_app_config('shop').get_models():
       if issubclass(model, models.Product) and model is not models.Product:
           products.append(model)

    result = []

    for product in products:
        qs = product.objects.filter(averageRate=averageRate, category=category)
        if len(qs)>0: result.append( qs )
    
    if len(result) > 0:
        return result[0][0]

    return None

def getFeedbacksByProductSlug(slug):

    product = getProductBySlug(slug)

    contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
    objectId = product.id

    feedbacks = models.Feedback.objects.filter(objectId=objectId, contentType=contentType)

    return feedbacks

def getProductAvarageRateBySlug(slug):

    product = getProductBySlug(slug)

    contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
    objectId = product.id

    feedbacks = models.Feedback.objects.filter(objectId=objectId, contentType=contentType)
    print(len(feedbacks))

    avarageRate = feedbacks.aggregate(Avg('rate'))['rate__avg']

    return avarageRate

def getTopProducts():

    products = []
    allQsProducts = []
    topProducts = []
    for model in apps.get_app_config('shop').get_models():
       if issubclass(model, models.Product) and model is not models.Product:
           products.append(model)

    for product in products:
        qs = product.objects.all()
        if len(qs)>0: allQsProducts.append( qs )

    
    for qs in allQsProducts:
        maxAvarageRate = ( qs.aggregate(Max('averageRate'))['averageRate__max'])
        topProducts.append(getProductByRate(maxAvarageRate, qs[0].category))
            
    return topProducts

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

        empty = False
        if len(result)==0: empty = True

        context = {'category':category_, 'qs_products': result, 'empty':empty}

    except models.Category.DoesNotExist: 
        return redirectToMainPage(request)
    
    return render(request, 'shop/category_page.html', context)

def getProductDetails(request, slug):
    
    product = getProductBySlug(slug)

    productFeedbacks = getFeedbacksByProductSlug(slug)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():

            # get current use id
            id = request.user.id
            if id == None:
                return HttpResponse("user is not authorized")

            # read fields
            comment = form.cleaned_data['comment']
            rate = form.cleaned_data['rate']

            # get product with specified slug
            product = getProductBySlug(slug)

            # fill ContentType foreign key
            contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
            objectId = product.id
            contentObject = product

            models.Feedback.objects.create(name=request.user.username, \
                                contentType=contentType,
                                objectId=objectId,
                                contentObject=contentObject,
                                comment=comment,
                                rate=rate)

            if(len(productFeedbacks)>0):
                product.averageRate=getProductAvarageRateBySlug(slug)
                product.save()

            return redirect('/products/{}/'.format(slug))
    else:
        form = FeedbackForm()


    if product != None:

        context = { 'product':product, 'form':form, 'productFeedbacks':productFeedbacks}

        return render(request, 'shop/product_page.html', context)

    return redirectToMainPage(request)

def cartPage(request):

    # newCart = CartProduct.objects.create(user=,contentType=,objectId=)
    return HttpResponse("Cart page")