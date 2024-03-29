from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from . import models
from django.db.models import Avg, Max
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
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

    if DEBUG: print("getCartProductsByUserId() return None")

    return None

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


def generateHeaderContext(request):

    context = {}
    if not request.user.is_anonymous:
        account = get_object_or_404(ProfileUser, user=request.user)
        orders_cart = models.CartProduct.objects.filter(user=request.user)

        amount_cart = 0
        totalPrice = 0
        for i in orders_cart:
            amount_cart += i.count
            totalPrice += i.price
        context = {
            'account':account,
            'amount_cart': amount_cart,
            'products_cart': orders_cart,
            'totalPrice': totalPrice
        }

    return context

def formContext(request, context):
    formedContext = {}
    formedContext.update(generateHeaderContext(request))
    formedContext.update(context)

    return formedContext


def mainPage(request):
    if request.method == 'POST':
        query = request.POST.get('searchInput', 'notFound')
        if query != "" and query != "notFound":
            return redirect('/search/' + query)

    topProducts = getTopProducts()
    # categories = models.Category.objects.all()

    categories = getValidCategories()
    for i in categories:
        print(str(i.categoryObject.slug)+'------------------------------------------')
    emptyCategorys = False
    emptyTopProducts = False
    if len(topProducts) == 0: emptyTopProducts = True
    if len(categories) == 0: emptyCategorys = True


    context={'categories':categories, 'topProducts':topProducts, 'emptyCategorys':emptyCategorys, 'emptyTopProducts':emptyTopProducts}
    context = formContext(request, context)
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
        query = request.POST.get('searchInput', 'notFound')
        if query != "" and query != "notFound":
            return redirect('/search/' + query)

        form = FeedbackForm(request.POST)
        if form.is_valid():
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

        fields = getProductMetaDataBySlug(slug)[1]
        
        del fields[-1]

        context={
            'product':product, 
            'form':form, 
            'productFeedbacks':productFeedbacks, 
            'empty':empty,
            'fields': fields[11::]
        }

        context = formContext(request, context)
        return render(request, 'shop/product_page.html', context)
    # except: return redirectToMainPage(request)


def adminDeleteComment(request, id, slug):

    feedbackToDelete = models.Feedback.objects.get(id = id)
    feedbackToDelete.delete()

    product = getProductBySlug(slug)

    product.averageRate=getProductAvarageRateBySlug(slug)
    product.save()
    
    return redirect('/products/{}/'.format(slug))


# render catalog for specified category 
def getCategoryCatalog(request, slug):
    if request.method == 'POST':
        query = request.POST.get('searchInput', 'notFound')
        if query != "" and query != "notFound":
            return redirect('/search/' + query)

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
        
        context={
            'category':category_, 
            'qs_products': result
        }

    except models.Category.DoesNotExist:
        if DEBUG: print("getCategoryCatalog() redirect ")

        return redirectToMainPage(request)
    
    context = formContext(request, context)

    if DEBUG: print("getCategoryCatalog() context: {}: ".format(context))
    return render(request, 'shop/category_page.html', context)


# add product with specified slug to cart
def addToCart(request, slug):
    # get current user
    user = request.user
    if user.id == None:
        if DEBUG: print("addToCart() Anonymous user")

        return HttpResponse('User is not authorized')

    product = getProductBySlug(slug)
    cartProduct = getCartProductByUserIdBySlug(user.id, slug)
    if cartProduct == None:
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
        cartProduct.count += 1
        cartProduct.price += cartProduct.contentObject.price
        cartProduct.save()

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

    context = formContext(request, context)

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
        query = request.POST.get('searchInput', 'notFound')
        if query != "" and query != "notFound":
            return redirect('/search/' + query)

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

            account = get_object_or_404(ProfileUser, user=request.user)

            cartProducts = 0
            obj = {
                'product':product,
                'cartProducts': cartProducts, 
                'deliveryAddress': deliveryAddress,
                'user': account,
                'totalPrice': product.price
            }

            message = get_template('user/email_form.html').render(obj)
            msg = EmailMessage('#techyRoom', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            msg.content_subtype = "html"
            msg.send()

            if DEBUG: print("getOrderProduct() ordered")

            return HttpResponseRedirect("/")
    else:
        form = OrderForm()

    context = {'form': form, 'product': product}

    context = formContext(request, context)

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
        query = request.POST.get('searchInput', 'notFound')
        if query != "" and query != "notFound":
            return redirect('/search/' + query)

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

            cartProductsNotContent = []
            account = get_object_or_404(ProfileUser, user=request.user)
            totalPrice = 0

            for i in cartProducts:
                totalPrice += i.price
                model = i.contentType.model_class()
                product = model.objects.get(id=i.objectId)

                order = {
                    'product': product
                }
                cartProductsNotContent.append(order)
            
            obj = {
                'products': cartProductsNotContent,
                'cartProducts': cartProducts, 
                'deliveryAddress': deliveryAddress,
                'user': account,
                'totalPrice': totalPrice
            }

            message = get_template('user/email_form.html').render(obj)
            msg = EmailMessage('#techyRoom', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            msg.content_subtype = "html"
            msg.send()

            for cartProduct in cartProducts:
                print(cartProduct)

            for cartProduct in cartProducts:
                cartProduct.delete()

            if DEBUG: print("getOrderCart() ordered")

            return HttpResponseRedirect("/")
    else:
        form = OrderForm()

    summary = 0
    for cartProduct in cartProducts:
        summary += cartProduct.price

    context = {'form': form, 'cartProducts': cartProducts, 'summary': summary}

    if DEBUG: print("getOrderCart() context: {} cartProducts: {} summary: {}".format(form, cartProducts, summary))
    context = formContext(request, context)

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
    
    productDictionary = []
    for field in product._meta.get_fields():
        fieldName = field.name
        fieldObject = product._meta.get_field(fieldName)
        fieldName = fieldObject.verbose_name
        fieldValue = fieldObject.value_from_object(product)

        productDictionary.append([fieldName, fieldValue])

    productData = [product, productDictionary]

    return productData


def searchProducts(searchQuery):
    productsMetaData = getAllProductsMetaData()

    foundProducts = []
    for productMetaData in productsMetaData:
        productObject = productMetaData[0]
        productMeta = productMetaData[1]

        for field in productMeta:
            if searchQuery.lower() in str(field[1]).lower():
                foundProducts.append(productObject)
                break

    print(foundProducts)

    if len(foundProducts) > 0:
        return foundProducts

    return None


def getWantedProducts(request, query):
    if request.method == 'POST':
        query = request.POST.get('searchInput', 'notFound')

        if query != "" and query != "notFound":
            return redirect('/search/' + query)

    print('Query: ' + str(query))

    products = searchProducts(query)

    context={
        'products': products
    }

    context = formContext(request, context)
    return render(request, 'shop/searchresult_page.html', context)


def getAllProducts():
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

    return products


def getAllCategories():
    categories = list(models.Category.objects.all())

    return categories


def getAllCategoryCatalogs():
    categories = getAllCategories()
    products = getAllProducts()

    categoryCatalogs = []

    for category in categories:
        categoryCatalogs.append([category, []])

    # divide products by categories
    for product in products:
        for categoryCatalog in categoryCatalogs:
            if categoryCatalog[0] == product.category:
                categoryCatalog[1].append(product)
                break

    return categoryCatalogs


class ValidCategory:
    categoryObject = None
    image = None

    def __init__(self, categoryObject, image):
        self.categoryObject = categoryObject
        self.image = image


def getValidCategories():

    categoryCatalogs = getAllCategoryCatalogs()
    categories = []

    for categoryCatalog in categoryCatalogs:
        if len(categoryCatalog[1]) > 0:
            validCategory = ValidCategory(categoryCatalog[0], categoryCatalog[1][0].image)
            categories.append(validCategory)


    return categories



def deleteCartProduct(request, id):
    try:
        cartProduct = models.CartProduct.objects.get(id=id)
    except:
        return HttpResponse('FATAL ERROR!')

    cartProduct.delete()

    return redirect(request.headers['Referer'][21::])


def deleteProduct(request, slug):
    product = getProductBySlug(slug)
    product.delete()

    return redirectToMainPage(request)