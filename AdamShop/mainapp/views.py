from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View

from accounts.models import User
from accounts.forms import UserChangeForm
from mainapp.forms import CartItemForm
from mainapp.models import Product, ProductImagesSet, WishList, CartItem


class IndexPage(View):
    def get(self, request):
        products = Product.objects.all()
        single_product_on_sale = Product.objects.filter(on_sale=True)[:1]
        products_on_sale = Product.objects.filter(on_sale=True)[1:3]
        context = {
            'products_on_sale': products_on_sale,
            'products': products,
            'single_product_on_sale': single_product_on_sale
        }
        return render(request, 'mainapp/index.html', context)


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


class CreateCartItem(CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'mainapp/create_cartitem.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.product_id = self.request.POST['product_id']
        object.quantity_of_products = self.request.POST['quantity_of_products']
        object.save()
        return super().form_valid(form=form)


class CartItemUpdate(UpdateView):
    model = CartItem
    fields = ('quantity_of_products',)
    template_name = 'mainapp/cart_item_update.html'
    success_url = '/'




