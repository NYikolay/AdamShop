from datetime import datetime, timedelta
import pytz

from django.db import models

from polymorphic.models import PolymorphicModel

from accounts.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_item', verbose_name='User')
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

    def get_subtotal_count(self):
        product_price = 0
        if self.product.on_sale:
            product_price = self.product.get_discount_price()
        else:
            product_price = self.product.price
        return self.quantity_of_products * product_price


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
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brands', verbose_name='Product Brand')
    market_launch_date = models.CharField(max_length=15, verbose_name='Market launch date')
    slug = models.SlugField('Product slug')
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 related_name='categories',
                                 verbose_name='Product category')
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
    on_sale = models.BooleanField(null=True, blank=True, verbose_name='Product on sale')
    discount_percent = models.FloatField(null=True, blank=True, verbose_name='Percent of discount')
    discount_time = models.DateTimeField(null=True, blank=True, verbose_name='Discount end in')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # Метод для определения действительна ли скидка, если нет - меняет значение on_sale на False,
    # в противном случае рассчитывает сумму скидки с учетом процента
    def get_discount_price(self):
        utc = pytz.UTC
        now = utc.localize(datetime.now()) - timedelta(hours=3)
        disc_time = self.discount_time
        if now > disc_time:
            self.on_sale = False
            self.save()
        elif self.on_sale and self.discount_percent:
            discount_price = (self.discount_percent / 100) * self.price
            return self.price - discount_price
        else:
            return 'There is no discount'

    def get_rating_stars(self):
        stars_list = [i for i in range(1, int(self.product_rating) + 1)]
        return stars_list

    def __str__(self):
        return self.name


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


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews', verbose_name='Review Creator')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Product')
    rating = models.IntegerField()
    body = models.TextField(max_length=700, verbose_name='Product review text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation review')

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f'Review from {self.user} to {self.product.name}'

    def get_rating_stars(self):
        stars_list = [i for i in range(1, int(self.rating) + 1)]
        return stars_list


class ProductReviewReply(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_reviews_reply',
                             verbose_name='Reply Creator')
    review = models.ForeignKey(ProductReview,
                               on_delete=models.CASCADE,
                               related_name='reviews_reply',
                               verbose_name='Reply')
    body = models.TextField(max_length=700, verbose_name='Reply review text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation reply')

    class Meta:
        verbose_name = 'Reply to review'
        verbose_name_plural = 'Reply to reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f'Reply from {self.user} to {self.review.user}, product {self.review.product.name}'


class ProductImagesSet(models.Model):
    image = models.ImageField(default='no_image.jpg')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images',
                                verbose_name='Product')
    main_img = models.BooleanField(null=True, blank=True, verbose_name='Main image')

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images set'
        ordering = ['product', ]

    def __str__(self):
        return f'Image for {self.product}'








