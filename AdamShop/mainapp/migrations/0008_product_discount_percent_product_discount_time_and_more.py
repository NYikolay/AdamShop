# Generated by Django 4.0.4 on 2022-05-28 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0007_cartitem_delete_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of discount'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Discount end in'),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(blank=True, null=True, verbose_name='Product on sale'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.DeleteModel(
            name='ProductOnSale',
        ),
    ]
