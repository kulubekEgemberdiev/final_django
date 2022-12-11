from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from shop.forms import RegisterForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegistrationUser(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class UserProfile(DetailView):
    model = get_user_model()
    template_name = "account/profile.html"
