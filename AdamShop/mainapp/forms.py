from django import forms

from mainapp.models import CartItem, WishList


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity_of_products',)


class WishItemForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ('quantity_of_products', )
