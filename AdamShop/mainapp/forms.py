from django import forms

from mainapp.models import CartItem, WishList, ProductReview, ProductReviewReply


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'


class WishItemForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ReplyOnReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReviewReply
        fields = '__all__'
