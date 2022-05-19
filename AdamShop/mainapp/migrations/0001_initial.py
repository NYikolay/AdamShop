# Generated by Django 4.0.4 on 2022-05-19 13:53

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('slug', models.SlugField(verbose_name='Product slug')),
                ('product_code', models.CharField(max_length=255, verbose_name='Product code')),
                ('description', models.TextField(max_length=600)),
                ('price', models.FloatField(verbose_name='Product price')),
                ('sale_price', models.FloatField(blank=True, null=True, verbose_name='Product sale price')),
                ('end_sale', models.DateTimeField(blank=True, null=True, verbose_name='Time of sale')),
                ('product_rating', models.FloatField(default=0)),
                ('color', models.CharField(max_length=56, verbose_name='Product color')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category Name')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductImagesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no_image.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56, verbose_name='Tag name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='SmartSpeaker',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.product')),
                ('market_launch_date', models.CharField(max_length=15, verbose_name='Market launch date')),
                ('type', models.CharField(max_length=56, verbose_name='Type')),
                ('nutrition', models.CharField(max_length=56, verbose_name='Nutrition')),
                ('memory_card_support', models.BooleanField()),
                ('number_of_speakers', models.CharField(max_length=25, verbose_name='Number of speakers')),
                ('min_frequency_range', models.FloatField(verbose_name='Min. Frequency range')),
                ('max_frequency_range', models.FloatField(verbose_name='Max. Frequency range')),
                ('bluetooth', models.BooleanField(verbose_name='Bluetooth ')),
                ('wifi', models.BooleanField(verbose_name='WiFi')),
                ('battery_capacity', models.PositiveIntegerField(verbose_name='Battery capacity')),
                ('battery_life', models.PositiveIntegerField(verbose_name='Max. battery life')),
                ('height', models.PositiveIntegerField(verbose_name='height')),
                ('width', models.PositiveIntegerField(verbose_name='width')),
                ('depth', models.PositiveIntegerField(verbose_name='depth')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('equipment', models.CharField(max_length=256, verbose_name='Equipment')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('mainapp.product',),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('body', models.TextField(max_length=700, verbose_name='Product review text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Review Creator')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='Product category'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productimagesset', verbose_name='Product image'),
        ),
        migrations.AddField(
            model_name='product',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
