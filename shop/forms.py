from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}
                               ))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}
                                ))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}
                                ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']