# Generated by Django 3.1.5 on 2021-01-25 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('display', models.CharField(max_length=255, verbose_name='Display type')),
                ('moistureProtection', models.CharField(max_length=32, verbose_name='Moisture protection')),
                ('material', models.CharField(max_length=32, verbose_name='Material')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Smarphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('diagonal', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Diagonal')),
                ('display', models.CharField(max_length=255, verbose_name='Display type')),
                ('screenResolution', models.CharField(max_length=32, verbose_name='Screen resolution')),
                ('processor', models.CharField(max_length=255, verbose_name='Processor')),
                ('ramSize', models.PositiveIntegerField(verbose_name='Ram size')),
                ('storageCapacity', models.PositiveIntegerField(verbose_name='Storage capacity')),
                ('moistureProtection', models.CharField(max_length=32, verbose_name='Moisture protection')),
                ('autonomyTime', models.PositiveIntegerField(verbose_name='Autonomy time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('processor', models.CharField(max_length=255, verbose_name='Processor')),
                ('ramType', models.CharField(max_length=255, verbose_name='Ram type')),
                ('ramSize', models.PositiveIntegerField(verbose_name='Ram size')),
                ('videoAdapter', models.CharField(max_length=255, verbose_name='Videocard')),
                ('storageType', models.CharField(max_length=32, verbose_name='Storage type')),
                ('storageCapacity', models.PositiveIntegerField(verbose_name='Storage capacity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectId', models.PositiveIntegerField()),
                ('deliveryAddress', models.CharField(max_length=255, verbose_name='Delivery address')),
                ('payment', models.CharField(max_length=255, verbose_name='Payment')),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('sensor', models.CharField(max_length=128, verbose_name='Sensor')),
                ('sensorDpi', models.PositiveIntegerField(verbose_name='Sensor dpi')),
                ('autonomyTime', models.PositiveIntegerField(verbose_name='Autonomy time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('diagonal', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Diagonal')),
                ('display', models.CharField(max_length=255, verbose_name='Display type')),
                ('displayFrequency', models.PositiveIntegerField(verbose_name='Dispay frequency')),
                ('screenResolution', models.CharField(max_length=32, verbose_name='Screen resolution')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LaptopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('diagonal', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Diagonal')),
                ('display', models.CharField(max_length=255, verbose_name='Display type')),
                ('screenResolution', models.CharField(max_length=32, verbose_name='Screen resolution')),
                ('processor', models.CharField(max_length=255, verbose_name='Processor')),
                ('ramType', models.CharField(max_length=255, verbose_name='Ram type')),
                ('ramSize', models.PositiveIntegerField(verbose_name='Ram size')),
                ('videoAdapter', models.CharField(max_length=255, verbose_name='Videocard')),
                ('storageType', models.CharField(max_length=255, verbose_name='Storage type')),
                ('storageCapacity', models.PositiveIntegerField(verbose_name='Storage capacity')),
                ('autonomyTime', models.PositiveIntegerField(verbose_name='Autonomy time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('type', models.CharField(max_length=128, verbose_name='Type')),
                ('switchType', models.CharField(max_length=128, verbose_name='Switch type')),
                ('autonomyTime', models.PositiveIntegerField(verbose_name='Autonomy time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Headphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('type', models.CharField(max_length=128, verbose_name='Type')),
                ('dynamicSize', models.PositiveIntegerField(verbose_name='Dynamic size')),
                ('autonomyTime', models.PositiveIntegerField(verbose_name='Autonomy time')),
                ('minFrequency', models.PositiveIntegerField(verbose_name='Minimal frequency')),
                ('maxFrequency', models.PositiveIntegerField(verbose_name='Maximal frequency')),
                ('resistance', models.PositiveIntegerField(verbose_name='Resistance')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='User name')),
                ('objectId', models.PositiveIntegerField()),
                ('comment', models.TextField(verbose_name='Comment')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=1, verbose_name='Rate')),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectId', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('count', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Count')),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model')),
                ('slug', models.SlugField(default='null', unique=True)),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('averageRate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, verbose_name='Average rate')),
                ('availability', models.BooleanField(verbose_name='Availability')),
                ('producer', models.CharField(max_length=64, verbose_name='Producer')),
                ('producerCountry', models.CharField(max_length=64, verbose_name='Producer country')),
                ('type', models.CharField(max_length=128, verbose_name='Type')),
                ('matrixSize', models.PositiveIntegerField(verbose_name='Matrix size')),
                ('megaPixels', models.PositiveIntegerField(verbose_name='Mega pixels')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
