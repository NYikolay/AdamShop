from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.models import User
from accounts.forms import UserChangeForm


def index(request):
    return render(request, 'mainapp/index.html', context={})


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


