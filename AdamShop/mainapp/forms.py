from django import forms

from mainapp.models import CartItem, WishList, ProductReview, ProductReviewReply


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity_of_products',)


class WishItemForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ('quantity_of_products', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('body', )


class ReplyOnReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReviewReply
        fields = ('body', )