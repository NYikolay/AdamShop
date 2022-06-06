from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View

from accounts.models import User
from accounts.forms import UserChangeForm
from mainapp.forms import CartItemForm, WishItemForm
from mainapp.models import Product, ProductImagesSet, WishList, CartItem, ProductCategory, Brand


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


class EmptyPage(View):
    def get(self, request):
        return render(request, 'mainapp/404_page.html', context={})


class DeleteCartItem(LoginRequiredMixin, DeleteView):
    model = CartItem
    template_name = 'mainapp/delete_purchase.html'
    success_url = '/'
    login_url = 'login'


class CreateCartItem(LoginRequiredMixin, View):
    form_class = CartItemForm
    template_name = 'index'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = request.user
            cart_item.product_id = request.POST.get('product_id')
            cart_item.quantity_of_products = request.POST.get('quantity_of_products')
            cart_item.save()
            return redirect(request.META.get('HTTP_REFERER'))


class CartItemUpdate(LoginRequiredMixin, UpdateView):
    model = CartItem
    fields = ('quantity_of_products',)
    template_name = 'mainapp/cart_item_update.html'
    success_url = '/'
    login_url = 'login'


class CreateWishItem(LoginRequiredMixin, View):
    form_class = WishItemForm
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            wish_item = form.save(commit=False)
            wish_item.user = request.user
            wish_item.product_id = request.POST.get('product_id')
            wish_item.quantity_of_products = request.POST.get('quantity_of_products')
            wish_item.save()
            return redirect(request.META.get('HTTP_REFERER'))


class DeleteWish(LoginRequiredMixin, DeleteView):
    model = WishList
    template_name = 'mainapp/delete_wish.html'
    success_url = '/'


class AccountPage(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'mainapp/account_page.html'
    login_url = 'login'

    def test_func(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return self.request.user == user


class AccountDetailsUpdate(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'mainapp/account_details-update.html'
    form_class = UserChangeForm
    login_url = 'login'

    def test_func(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return self.request.user == user

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('account_details', kwargs={'pk': pk})


class ProductsPage(View):
    template = 'mainapp/products_page.html'

    def get(self, request):
        brands = Brand.objects.all()
        categories = ProductCategory.objects.all()
        products = Product.objects.all().order_by('-date_of_receipt')
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        try:
            context = {
                'all_products': products,
                'current_products': paginator.page(page),
                'current_page': page,
                'pages': paginator,
                'categories': categories,
                'brands': brands,
            }
        except:
            return redirect('404_page')
        return render(request, self.template, context)



