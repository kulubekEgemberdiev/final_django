from django import forms
from django.forms import widgets

from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description',
                  'trademark', 'product_type',
                  'maker', 'price', 'image',
                  'qty_in_stock', 'category'
                  ]

        widgets = {
            'category': widgets.RadioSelect,
            'description': widgets.Textarea(attrs={"cols": 50, "rows": 2}),
        }
