# Generated by Django 4.0.4 on 2022-05-19 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_smartphone_remove_smartspeaker_market_launch_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='mainapp.producttag', verbose_name='Tag'),
            preserve_default=False,
        ),
    ]