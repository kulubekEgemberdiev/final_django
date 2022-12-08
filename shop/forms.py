from django import forms
from django.forms import widgets

from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
