from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm

from .models import *





class LaptopAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MonitorAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='monitors'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PersonalComputerAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='personal_computer'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class HeadphonesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='headphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class KeyboardAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='keyboards'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MouseAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mice'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CameraAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='cameras'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SmartwatchAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartwatches'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



# Register your models here.
admin.site.register(Category)

admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(PersonalComputer, PersonalComputerAdmin)
admin.site.register(Headphones, HeadphonesAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
admin.site.register(Mouse, MouseAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)

admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(Feedback)