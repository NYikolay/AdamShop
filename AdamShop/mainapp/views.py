from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.models import User
from accounts.forms import UserChangeForm
from mainapp.models import Product, ProductImagesSet, WishList, CartItem


class IndexPage(ListView):
    model = Product
    template_name = 'mainapp/index.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     kwargs = super(IndexPage, self).get_context_data(**kwargs)
    #     kwargs.update({
    #         'image_set': ProductImagesSet.objects.all(),
    #     })
    #     return kwargs


class AccountPage(DetailView):
    model = User
    template_name = 'mainapp/account_page.html'


class AccountDetailsUpdate(UpdateView):
    model = User
    template_name = 'mainapp/account_details-update.html'
    form_class = UserChangeForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('account_details', kwargs={'pk': pk})


class DeleteWish(DeleteView):
    model = WishList
    template_name = 'mainapp/delete_wish.html'
    success_url = '/'


class DeleteCartItem(DeleteView):
    model = CartItem
    template_name = 'mainapp/delete_purchase.html'
    success_url = '/'




