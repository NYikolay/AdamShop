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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation review')


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name', )

    def __str__(self):
        return self.name


class ProductImagesSet(models.Model):
    image = models.ImageField(default='no_image.jpg')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product')


class Product(PolymorphicModel):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    type = models.CharField(max_length=56, verbose_name='Type')
    market_launch_date = models.CharField(max_length=15, verbose_name='Market launch date')
    slug = models.SlugField('Product slug')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product category')
    tag = models.ForeignKey(ProductTag, on_delete=models.PROTECT, verbose_name='Tag')
    product_code = models.CharField(max_length=255, verbose_name='Product code')
    description = models.TextField(max_length=600)
    price = models.FloatField('Product price')
    sale_price = models.FloatField(null=True, blank=True, verbose_name='Product sale price')
    end_sale = models.DateTimeField(null=True, blank=True, verbose_name='Time of sale')
    product_rating = models.FloatField(default=0)
    color = models.CharField(max_length=56, verbose_name='Product color')


class SmartSpeaker(Product):
    nutrition = models.CharField(max_length=56, verbose_name='Nutrition')
    memory_card_support = models.BooleanField()
    number_of_speakers = models.CharField(max_length=25, verbose_name='Number of speakers')
    min_frequency_range = models.FloatField(verbose_name='Min. Frequency range')
    max_frequency_range = models.FloatField(verbose_name='Max. Frequency range')
    bluetooth = models.BooleanField(verbose_name='Bluetooth ')
    wifi = models.BooleanField(verbose_name='WiFi')
    battery_capacity = models.PositiveIntegerField(verbose_name='Battery capacity')
    battery_life = models.PositiveIntegerField(verbose_name='Max. battery life')
    height = models.PositiveIntegerField(verbose_name='height')
    width = models.PositiveIntegerField(verbose_name='width')
    depth = models.PositiveIntegerField(verbose_name='depth')
    weight = models.FloatField(verbose_name='weight')
    equipment = models.CharField(max_length=256, verbose_name='Equipment')


class SmartPhone(Product):
    screen_technology = models.CharField(max_length=65, verbose_name='Screen technology')
    operating_system = models.CharField(max_length=65, verbose_name='Operating sistem')
    os_version = models.CharField(max_length=65, verbose_name='OS version')
    screen_size = models.FloatField(verbose_name='Screen Size')
    screen_resolution = models.CharField(max_length=65, verbose_name='Screen resolution')
    ram = models.PositiveIntegerField()
    built_in_memory = models.PositiveIntegerField()
    cpu = models.CharField(max_length=255, verbose_name='CPU')
    num_of_cores = models.PositiveIntegerField()








