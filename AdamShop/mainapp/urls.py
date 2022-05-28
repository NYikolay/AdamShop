from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from mainapp.views import IndexPage, AccountPage, AccountDetailsUpdate, DeleteWish, DeleteCartItem, CreateCartItem, CartItemUpdate

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('account/<int:pk>', AccountPage.as_view(), name='account_page'),
    path('account_details/<int:pk>', AccountDetailsUpdate.as_view(), name='account_details'),
    path('delete_wish/<int:pk>', DeleteWish.as_view(), name='delete_wish'),
    path('delete_purchase/<int:pk>', DeleteCartItem.as_view(), name='delete_cart_item'),
    path('create_cart_item/', CreateCartItem.as_view(), name='create_cart_item'),
    path('cart_item_update/<int:pk>/', CartItemUpdate.as_view(), name='cart_item_update'),
    path('change_password/',
         PasswordChangeView.as_view(
             template_name='mainapp/change_password.html',
             success_url=reverse_lazy('password_change_done')
         ),
         name='password_change'
         ),
    path('change_password/done/', PasswordChangeDoneView.as_view(
        template_name='mainapp/password_change_done.html'
    ),
         name='password_change_done')

]
