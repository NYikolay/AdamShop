from django.urls import path as url, reverse_lazy
from django.contrib.auth.views import \
    PasswordChangeView, \
    PasswordChangeDoneView

from mainapp.views import \
    IndexPage, \
    AccountPage, \
    AccountDetailsUpdate, \
    DeleteWish, \
    DeleteCartItem, \
    CreateCartItem, \
    CartItemUpdate, \
    CreateWishItem, \
    ProductsPage, \
    EmptyPage

urlpatterns = [
    url('', IndexPage.as_view(), name='index'),
    url('account/<int:pk>', AccountPage.as_view(), name='account_page'),
    url('404_not_found/', EmptyPage.as_view(), name='404_page'),
    url('account_details/<int:pk>', AccountDetailsUpdate.as_view(), name='account_details'),
    url('delete_wish/<int:pk>', DeleteWish.as_view(), name='delete_wish'),
    url('create_wish_item/', CreateWishItem.as_view(), name='create_wish_item'),
    url('delete_purchase/<int:pk>', DeleteCartItem.as_view(), name='delete_cart_item'),
    url('create_cart_item/', CreateCartItem.as_view(), name='create_cart_item'),
    url('cart_item_update/<int:pk>/', CartItemUpdate.as_view(), name='cart_item_update'),
    url('products_page/', ProductsPage.as_view(), name='products_page'),
    url('change_password/',
        PasswordChangeView.as_view(
            template_name='mainapp/change_password.html',
            success_url=reverse_lazy('password_change_done')
        ),
        name='password_change'
        ),
    url('change_password/done/', PasswordChangeDoneView.as_view(
        template_name='mainapp/password_change_done.html'
    ),
        name='password_change_done')

]
