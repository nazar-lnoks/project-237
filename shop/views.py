from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from . import models
from django.db.models import Avg, Max

from django.contrib.contenttypes.models import ContentType

from django.apps import apps

from .forms import FeedbackForm, OrderForm
from user.models import ProfileUser

DEBUG = 1

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

    if product is None: return 0

    contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
    objectId = product.id

    feedbacks = models.Feedback.objects.filter(objectId=objectId, contentType=contentType)
    # print(len(feedbacks))

    if(len(feedbacks) == 0): avarageRate = 0
    else: avarageRate = feedbacks.aggregate(Avg('rate'))['rate__avg']

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

def mainPage(request):

    topProducts = getTopProducts()
    categories = models.Category.objects.all()

    emptyCategorys = False
    emptyTopProducts = False
    if len(topProducts) == 0: emptyTopProducts = True
    if len(categories) == 0: emptyCategorys = True
    
    if request.user.is_anonymous:
        context={
            'categories':categories, 
            'topProducts':topProducts, 
            'emptyCategorys':emptyCategorys, 
            'emptyTopProducts':emptyTopProducts
        }
    else:
        account = get_object_or_404(ProfileUser, user=request.user)
        orders_cart = models.CartProduct.objects.filter(user=request.user)
        amount_cart = len(orders_cart)
        objects = []

        for i in orders_cart:
            model = i.contentType.model_class()
            product = model.objects.get(id=i.objectId)

            order = {
                'product': product
            }
            objects.append(order)
        context={
            'categories':categories, 
            'topProducts':topProducts, 
            'emptyCategorys':emptyCategorys, 
            'emptyTopProducts':emptyTopProducts, 
            'account':account,
            'amount_cart': amount_cart,
            'products_cart':objects
        }

    return render(request, 'shop/main_page.html', context)

def getCartProductByUserIdBySlug(id, slug):
    # get product object by slug
    product = getProductBySlug(slug)
    # get user object by id
    user = models.User.objects.get(id=id) 

    contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)

    product = models.CartProduct.objects.filter(user=user, contentType=contentType, objectId=product.id)
    if len(product) > 0:
        return product[0]

    if DEBUG: print("getCartProductsByUserId() return None")

    return None

def getProductDetails(request, slug):
    product = getProductBySlug(slug)
    productFeedbacks = getFeedbacksByProductSlug(slug)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():

            # print("---------------[" + request.POST.get('selected_rating') + "]-------------------------")
            

            # get current use id
            id = request.user.id
            if id == None:
                return HttpResponse("user is not authorized")

            # read fields
            comment = form.cleaned_data['comment']
            if not request.POST.get('selected_rating'): rate = 0
            else: rate = int(request.POST.get('selected_rating')) #form.cleaned_data['rate']

            

            # get product with specified slug
            product = getProductBySlug(slug)

            # fill ContentType foreign key
            contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
            objectId = product.id
            contentObject = product

            # creating feedback obj
            models.Feedback.objects.create(name=request.user.username, \
                                contentType=contentType,
                                objectId=objectId,
                                contentObject=contentObject,
                                comment=comment,
                                rate=rate)

            # calculate product average rate if there is at least 1 feedback
            if(len(productFeedbacks)>0):
                product.averageRate=getProductAvarageRateBySlug(slug)
                product.save()

            
            return redirect('/products/{}/'.format(slug))
    else:
        form = FeedbackForm()


    if product != None:

        empty = False
        if len(productFeedbacks)==0: empty = True
        
        context = { 'product':product, 'form':form, 'productFeedbacks':productFeedbacks, 'empty':empty}

        return render(request, 'shop/product_page.html', context)
    # except: return redirectToMainPage(request)

def cartPage(request):

    # newCart = CartProduct.objects.create(user=,contentType=,objectId=)
    return HttpResponse("Cart page")

def adminDeleteComment(request, id, slug):

    feedbackToDelete = models.Feedback.objects.get(id = id)
    feedbackToDelete.delete()

    product = getProductBySlug(slug)
    product.averageRate=getProductAvarageRateBySlug(slug)
    product.save()
    
    return redirect('/products/{}/'.format(slug))

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
        
        if request.user.is_anonymous:
            context={
                'category':category_, 
                'qs_products': result
            }
        else:
            account = get_object_or_404(ProfileUser, user=request.user)
            context={
                'category':category_, 
                'qs_products': result,
                'account':account
            }

    except models.Category.DoesNotExist:
        if DEBUG: print("getCategoryCatalog() redirect ")

        return redirectToMainPage(request)
    
    if DEBUG: print("getCategoryCatalog() context: {}: ".format(context))

    return render(request, 'shop/category_page.html', context)


# add product with specified slug to cart
def addToCart(request, slug):
    # get current user
    user = request.user
    if user.id == None:
        if DEBUG: print("addToCart() Anonymous user")

        return redirect('/products/{}/'.format(str(slug)))

    product = getCartProductByUserIdBySlug(user.id, slug)
    if product == None:
        # get product with specified slug
        product = getProductBySlug(slug)
        
        # fill ContentType foreign key
        contentType = ContentType.objects.get(app_label="shop", model=product._meta.model_name)
        objectId = product.id
        contentObject = product

        # create cart product object
        models.CartProduct.objects.create(user=request.user, \
                                        contentType=contentType, \
                                        objectId=objectId, \
                                        contentObject=contentObject, \
                                        price=product.price, \
                                        count=1)
    else:
        product.count += 1
        product.price += product.contentObject.price
        product.save()

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
                
                for i in range(int(cartProduct.count)):
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

    summary = 0
    for cartProduct in cartProducts:
        summary += cartProduct.price

    context = {'form': form, 'cartProducts': cartProducts, 'summary': summary}

    if DEBUG: print("getOrderCart() context: {} cartProducts: {} summary: {}".format(form, cartProducts, summary))

    return render(request, 'shop/ordercart_page.html', context)


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

def cartPage(request):
    return HttpResponse("Cart page")

def getAllProductsMetaData():
    productClasses = []
    for model in apps.get_app_config('shop').get_models():
       if issubclass(model, models.Product) and model is not models.Product:
           productClasses.append(model)

    productQueries = []
    for productClass in productClasses:
        productQueries.append(productClass.objects.all())

    products = []
    for productQuery in productQueries:
        for product in productQuery:
            products.append(product)


    productsData = []
    for product in products:
        productDictionary = []

        for field in product._meta.get_fields():
            fieldName = field.name
            fieldObject = product._meta.get_field(fieldName)
            fieldValue = fieldObject.value_from_object(product)

            productDictionary.append([fieldName, fieldValue])

        productsData.append([product, productDictionary])

    return productsData


def getProductMetaDataBySlug(slug):
    product = getProductBySlug(slug)
    
    productData = []
    productDictionary = []

    for field in product._meta.get_fields():
        fieldName = field.name
        fieldObject = product._meta.get_field(fieldName)
        fieldValue = fieldObject.value_from_object(product)

        productDictionary.append([fieldName, fieldValue])

    productData.append([product, productDictionary])

    return productData

def searchProduct(searchQuery):
    productsMetaData = getAllProductsMetaData()

    foundProducts = []
    for productMetaData in productsMetaData:
        productObject = productMetaData[0]
        productMeta = productMetaData[1]

        for field in productMeta:
            if searchQuery in str(field[1]):
                foundProducts.append(productObject)
                break

    print(foundProducts)

    if len(foundProducts) > 0:
        return foundProducts

    return None