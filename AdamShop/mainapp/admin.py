from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin, PolymorphicChildModelFilter, \
     PolymorphicInlineSupportMixin

from mainapp.models import *


class InlineProductImagesSet(admin.TabularInline):
    model = ProductImagesSet


class ModelProductChildAdmin(PolymorphicChildModelAdmin):
    base_model = Product


@admin.register(SmartSpeaker)
class SmartSpeakerAdmin(ModelProductChildAdmin):
    base_model = SmartSpeaker
    inlines = (InlineProductImagesSet,)


@admin.register(SmartPhone)
class SmartPhoneAdmin(ModelProductChildAdmin):
    base_model = SmartPhone
    inlines = (InlineProductImagesSet,)


@admin.register(Product)
class ModelProductParentAdmin(PolymorphicParentModelAdmin):
    base_model = Product
    child_models = (SmartSpeaker, SmartPhone)
    list_filter = (PolymorphicChildModelFilter, )


admin.site.register(ProductTag)
admin.site.register(ProductReview)
admin.site.register(ProductCategory)
admin.site.register(ProductImagesSet)
admin.site.register(Brand)
admin.site.register(ProductOnSale)
admin.site.register(CartItem)
admin.site.register(WishList)




