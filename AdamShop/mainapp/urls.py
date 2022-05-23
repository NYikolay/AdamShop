from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from mainapp.views import IndexPage, AccountPage, AccountDetailsUpdate, DeleteWish, DeleteCartItem

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('account/<int:pk>', AccountPage.as_view(), name='account_page'),
    path('account_details/<int:pk>', AccountDetailsUpdate.as_view(), name='account_details'),
    path('delete_wish/<int:pk>', DeleteWish.as_view(), name='delete_wish'),
    path('delete_purchase/<int:pk>', DeleteCartItem.as_view(), name='delete_cartitem'),
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
