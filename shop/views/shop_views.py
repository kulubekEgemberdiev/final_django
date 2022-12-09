from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

# from shop.forms import *
from shop.models import *


class Index(ListView):
    model = Products
    template_name = 'shop/index.html'


def about_page(request):
    return render(request, 'shop/about.html')



