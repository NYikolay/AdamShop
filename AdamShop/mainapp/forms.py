from django import forms

from mainapp.models import CartItem


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity_of_products',)
