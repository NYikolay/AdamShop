from django.db import models

from polymorphic.models import PolymorphicModel

from accounts.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items', verbose_name='User')
    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                related_name='cart_product',
                                verbose_name='Product')
    quantity_of_products = models.PositiveSmallIntegerField(default=1, verbose_name='Quantity of products')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
        ordering = ['-created_at']

    def __str__(self):
        return f'Purchase from {self.user}, product name: {self.product}, quantity: {self.quantity_of_products}'


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists', verbose_name='User')
    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                related_name='wishlists_product',
                                verbose_name='Product'
                                )
    quantity_of_products = models.PositiveSmallIntegerField(default=1, verbose_name='Quantity of products')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
        ordering = ['-created_at']

    def __str__(self):
        return f'From {self.user}: {self.product}, quantity: {self.quantity_of_products}'


class ProductTag(models.Model):
    name = models.CharField(max_length=56, verbose_name='Tag name')

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Brand name')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(PolymorphicModel):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Product Brand')
    market_launch_date = models.CharField(max_length=15, verbose_name='Market launch date')
    slug = models.SlugField('Product slug')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product category')
    tag = models.ManyToManyField(ProductTag, verbose_name='Tag')
    description = models.TextField(max_length=600, verbose_name='Product description')
    price = models.FloatField('Product price')
    date_of_receipt = models.DateTimeField(auto_now_add=True, verbose_name='Arrival')
    product_rating = models.FloatField(default=0, verbose_name='Product Rating')
    color = models.CharField(max_length=56, verbose_name='Product color')
    height = models.PositiveIntegerField(null=True, blank=True, verbose_name='height')
    width = models.PositiveIntegerField(null=True, blank=True, verbose_name='width')
    depth = models.PositiveIntegerField(null=True, blank=True, verbose_name='depth')
    weight = models.FloatField(null=True, blank=True, verbose_name='weight')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


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


class ProductOnSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sale', verbose_name='Product')
    discounted_price = models.FloatField()
    sale_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Review Creator')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    rating = models.IntegerField()
    body = models.TextField(max_length=700, verbose_name='Product review text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation review')


class ProductImagesSet(models.Model):
    image = models.ImageField(default='no_image.jpg')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Product')
    main_img = models.BooleanField(null=True, blank=True, verbose_name='Main image')

    class Meta:
        verbose_name = 'ProductImagesSet'
        verbose_name_plural = 'ProductImagesSets'
        ordering = ['product', ]

    def __str__(self):
        return f'Image for {self.product}'








