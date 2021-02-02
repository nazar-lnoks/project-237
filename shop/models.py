from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
from time import time

def gen_slug(model_):
    new_sl = slugify(model_, allow_unicode=True)
    return new_sl + '-' + str(int(time()))


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{}".format(self.name)

    
class Product(models.Model):
    class Meta:
        abstract = True

    model = models.CharField(max_length=45, verbose_name='Model')
    slug = models.SlugField(unique=True, default='null')
    description = models.CharField(max_length=1024, verbose_name='Description')
    image = models.ImageField(upload_to="products", verbose_name='Image')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    averageRate = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Average rate', default=0.0)
    availability = models.BooleanField(verbose_name='Availability')
    producer = models.CharField(max_length=64, verbose_name='Producer')
    producerCountry = models.CharField(max_length=64, verbose_name='Producer country')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.model)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.model)


class Laptop(Product):
    diagonal = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Diagonal')
    display = models.CharField(max_length=255, verbose_name='Display type')
    screenResolution = models.CharField(max_length=32, verbose_name='Screen resolution')
    processor = models.CharField(max_length=255, verbose_name='Processor')
    ramType = models.CharField(max_length=255, verbose_name='Ram type')
    ramSize = models.PositiveIntegerField(verbose_name='Ram size')
    videoAdapter = models.CharField(max_length=255, verbose_name='Videocard')
    storageType = models.CharField(max_length=255, verbose_name='Storage type')
    storageCapacity = models.PositiveIntegerField(verbose_name='Storage capacity')
    autonomyTime = models.PositiveIntegerField(verbose_name='Autonomy time')

    def __str__(self):
        return "{} {}".format(self.category.name, self.model)

class Monitor(Product):
    diagonal = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Diagonal')
    display = models.CharField(max_length=255, verbose_name='Display type')
    displayFrequency = models.PositiveIntegerField(verbose_name='Dispay frequency')
    screenResolution = models.CharField(max_length=32, verbose_name='Screen resolution')
    
    def __str__(self):
        return "{}".format(self.screenResolution)

class PersonalComputer(Product):
    processor = models.CharField(max_length=255, verbose_name='Processor')
    ramType = models.CharField(max_length=255, verbose_name='Ram type')
    ramSize = models.PositiveIntegerField(verbose_name='Ram size')
    videoAdapter = models.CharField(max_length=255, verbose_name='Videocard')
    storageType = models.CharField(max_length=32, verbose_name='Storage type')
    storageCapacity = models.PositiveIntegerField(verbose_name='Storage capacity')

    def __str__(self):
        return "{} {}".format(self.processor, self.ramSize)

class Headphones(Product):
    type = models.CharField(max_length=128, verbose_name='Type')
    dynamicSize = models.PositiveIntegerField(verbose_name='Dynamic size')
    autonomyTime = models.PositiveIntegerField(verbose_name='Autonomy time')
    minFrequency = models.PositiveIntegerField(verbose_name='Minimal frequency')
    maxFrequency = models.PositiveIntegerField(verbose_name='Maximal frequency')
    resistance = models.PositiveIntegerField(verbose_name='Resistance')

    def __str__(self):
        return "{} {} {}".format(self.type, self.minFrequency, self.maxFrequency)

class Keyboard(Product):
    type = models.CharField(max_length=128, verbose_name='Type')
    switchType = models.CharField(max_length=128, verbose_name='Switch type')
    autonomyTime = models.PositiveIntegerField(verbose_name='Autonomy time')

    def __str__(self):
        return "{} {}".format(self.type, self.switchType)

class Mouse(Product):
    sensor = models.CharField(max_length=128, verbose_name='Sensor')
    sensorDpi = models.PositiveIntegerField(verbose_name='Sensor dpi')
    autonomyTime = models.PositiveIntegerField(verbose_name='Autonomy time')

    def __str__(self):
        return "{}".format(self.sensorDpi)

class Smartphone(Product):
    diagonal = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Diagonal')
    display = models.CharField(max_length=255, verbose_name='Display type')
    screenResolution = models.CharField(max_length=32, verbose_name='Screen resolution')
    processor = models.CharField(max_length=255, verbose_name='Processor')
    ramSize = models.PositiveIntegerField(verbose_name='Ram size')
    storageCapacity = models.PositiveIntegerField(verbose_name='Storage capacity')
    moistureProtection = models.CharField(max_length=32, verbose_name='Moisture protection')
    autonomyTime = models.PositiveIntegerField(verbose_name='Autonomy time')

    def __str__(self):
        return "{} {}".format(self.storageCapacity, self.moistureProtection)

class Camera(Product):
    type = models.CharField(max_length=128, verbose_name='Type')
    matrixSize = models.PositiveIntegerField(verbose_name='Matrix size')
    megaPixels = models.PositiveIntegerField(verbose_name='Mega pixels')

    def __str__(self):
        return "{} {}".format(self.type, self.megaPixels)

class Smartwatch(Product):
    display = models.CharField(max_length=255, verbose_name='Display type')
    moistureProtection = models.CharField(max_length=32, verbose_name='Moisture protection')
    material = models.CharField(max_length=32, verbose_name='Material')

    def __str__(self):
        return "Smartwatch {}".format(self.id)


class CartProduct(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectId = models.PositiveIntegerField()
    contentObject = GenericForeignKey('contentType', 'objectId')

    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    count = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Count')

    def __str__(self):
        return "{}".format(self.contentType._meta.model_name)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='User', null=True, on_delete=models.SET_NULL)
    
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectId = models.PositiveIntegerField()
    contentObject = GenericForeignKey('contentType', 'objectId')
    date_buy = models.DateField(auto_now_add=True)

    deliveryAddress = models.CharField(max_length=255, verbose_name='Delivery address')
    payment = models.CharField(max_length=255, verbose_name='Payment')

    def __str__(self):
        return "Order {}".format(self.id)

    class Meta:
        ordering = ['-id']

class Feedback(models.Model):
    name = models.CharField(max_length=45, verbose_name='User name')
    
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectId = models.PositiveIntegerField()
    contentObject = GenericForeignKey('contentType', 'objectId')

    comment = models.TextField(verbose_name='Comment')
    rate = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Rate')

    def __str__(self):
        return "{}".format(self.name)












