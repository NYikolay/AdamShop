from django.db import models

from polymorphic.models import PolymorphicModel

from accounts.models import User


class ProductTag(models.Model):
    name = models.CharField(max_length=56, verbose_name='Tag name')

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Review Creator')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product')
    rating = models.IntegerField()
    body = models.TextField(max_length=700, verbose_name='Product review text')


class ProductCategory(models.Model):
    pass


class ProductImagesSet(models.Model):
    image = models.ImageField(default='no_image.jpg')


class Product(PolymorphicModel):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    slug = models.SlugField('Product slug')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product category')
    image = models.ForeignKey(ProductImagesSet, on_delete=models.CASCADE, verbose_name='Product image')
    product_code = models.CharField(max_length=255, verbose_name='Product code')
    description = models.TextField(max_length=600)
    price = models.FloatField('Product price')
    sale_price = models.FloatField(null=True, blank=True, verbose_name='Product sale price')
    end_sale = models.DateTimeField(null=True, blank=True, verbose_name='Time of sale')
    product_rating = models.FloatField(default=0)



