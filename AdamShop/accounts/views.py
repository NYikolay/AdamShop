from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.models import User
from accounts.forms import UserCreationForm


class Login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = 'index'


class Logout(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'login'


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().get(request, **kwargs)






