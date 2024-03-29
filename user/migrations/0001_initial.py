# Generated by Django 3.1.5 on 2021-01-26 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('name', models.CharField(db_index=True, max_length=45)),
                ('surname', models.CharField(db_index=True, max_length=60)),
                ('middlename', models.CharField(db_index=True, max_length=60)),
                ('birth_date', models.DateField(max_length=8)),
                ('image', models.ImageField(blank=True, upload_to='avatars/')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
