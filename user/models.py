from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=45, db_index=True)
    surname = models.CharField(max_length=60, db_index=True)
    middlename = models.CharField(max_length=60, db_index=True)
    birth_date = models.DateField(max_length=8)
    image = models.ImageField(upload_to="avatars/", blank=True)
    phone_number = PhoneNumberField(blank=True, help_text="Contact phone number")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify('user-' + self.name + self.id)
        super().save(*args, **kwargs)


    def __str__(self):
        return 'User: {} {} {}'.format(self.surname, self.name, self.middlename)