from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about-us/', about_page, name='about'),
    # -------------------------------------------------------------------------------------
    path('add-category/', AddCategory.as_view(), name='add_category'),
    path('categories/', Categories.as_view(), name='categories'),
    path('category-<int:pk>/edit/', EditCategory.as_view(), name='edit_category'),
    path('category-<int:pk>/delete/', DeleteCategory.as_view(), name='delete_category'),
]
