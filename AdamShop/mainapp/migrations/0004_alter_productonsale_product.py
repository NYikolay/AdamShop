# Generated by Django 4.0.4 on 2022-05-22 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_productimagesset_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productonsale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sale', to='mainapp.product', verbose_name='Product'),
        ),
    ]
