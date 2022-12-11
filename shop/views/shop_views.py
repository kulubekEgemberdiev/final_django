from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from shop.forms import ProductForm
from shop.models import Products, Category


class Index(ListView):
    model = Products
    template_name = 'shop/index.html'


def about_page(request):
    return render(request, 'shop/about.html')


class CreateProduct(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'shop/create_product.html'
    success_url = reverse_lazy('products_list')


# class ProductsList(ListView):
#     model = Products
#     template_name = 'shop/products_list.html'
#     context_object_name = 'products'
#     paginate_by = 9
#     paginate_orphans = 2
#     queryset = Products.objects.order_by('-id')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['category'] = Category.objects.all()
#         return context
#
#     def get_ordering(self):
#         ordering = Products.objects.filter(category_id=self.request.GET.get('order'))
#         return ordering

class ProductsList(ListView):
    model = Products
    paginate_by = 9
    paginate_orphans = 2
    template_name = 'shop/products_list.html'
    context_object_name = 'products'
    queryset = Products.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_ordering(self):
        self.queryset = Products.objects.filter(category_id=self.request.GET.get('sort'))
        return self.queryset


class ProductDetail(DetailView):
    template_name = "shop/detail_product.html"
    model = Products
    context_object_name = "product"


class ProductEdit(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'shop/update_product.html'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class DeleteProduct(DeleteView):
    template_name = "shop/delete_product.html"
    model = Products
    context_object_name = 'items'
    success_url = reverse_lazy('products_list')
