from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from shop.forms import *
from shop.models import *


class Categories(ListView):
    model = Category
    template_name = 'categories/categories.html'
    context_object_name = 'items'


class AddCategory(CreateView):
    form_class = CategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('categories')


class EditCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/update_category.html'
    success_url = reverse_lazy('categories')


class DeleteCategory(DeleteView):
    template_name = "categories/delete_category.html"
    model = Category
    context_object_name = 'items'
    success_url = reverse_lazy('categories')
