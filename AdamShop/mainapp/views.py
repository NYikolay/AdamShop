from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View

from accounts.models import User
from accounts.forms import UserChangeForm
from mainapp.forms import CartItemForm, WishItemForm, ReviewForm, ReplyOnReviewForm
from mainapp.models import Product, \
    ProductImagesSet, \
    WishList, \
    CartItem, \
    ProductCategory, \
    Brand, \
    ProductReview, \
    ProductReviewReply


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
        return render(request, '404_page.html')


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
            cart_item.user_id = request.POST.get('user')
            cart_item.product_id = request.POST.get('product')
            cart_item.quantity_of_products = request.POST.get('quantity_of_products')
            cart_item.save()
            return redirect(request.META.get('HTTP_REFERER'))


class CreateWishItem(LoginRequiredMixin, View):
    form_class = WishItemForm
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            wish_item = form.save(commit=False)
            wish_item.user_id = request.POST.get('user')
            wish_item.product_id = request.POST.get('product')
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


class SingleProductPage(View):
    template = 'mainapp/single_product_page.html'

    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
        except:
            return redirect('404_page')
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return redirect('404_page')
        context = {
            'product': product,
        }
        return render(request, self.template, context)


class CreateReview(LoginRequiredMixin, View):
    form_class = ReviewForm
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.POST.get('user')
            review.product_id = request.POST.get('product')
            review.rating = request.POST.get('rating')
            review.body = request.POST.get('body')
            review.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))


class DeleteReview(LoginRequiredMixin, DeleteView):
    model = ProductReview
    login_url = 'login'
    template_name = 'mainapp/delete_review.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url


class CreateReplyOnReview(LoginRequiredMixin, View):
    form_class = ReplyOnReviewForm
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user_id = request.POST.get('user')
            reply.review_id = request.POST.get('review')
            reply.body = request.POST.get('body')
            reply.save()
            return redirect(request.META.get('HTTP_REFERER'))


class DeleteReply(LoginRequiredMixin, DeleteView):
    model = ProductReviewReply
    login_url = 'login'
    template_name = 'mainapp/delete_reply.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url





