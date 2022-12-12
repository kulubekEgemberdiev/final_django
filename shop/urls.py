from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about-us/', about_page, name='about'),
    path('create-product/', CreateProduct.as_view(), name='create_product'),
    path('list-products/', ProductsList.as_view(), name='products_list'),
    path('product-<int:pk>/detail/', ProductDetail.as_view(), name='product_detail'),
    path('product-<int:pk>/edit/', ProductEdit.as_view(), name='product_edit'),
    path('product-<int:pk>/delete/', DeleteProduct.as_view(), name='product_delete'),
    # -------------------------------------------------------------------------------------
    path('add-category/', AddCategory.as_view(), name='add_category'),
    path('categories/', Categories.as_view(), name='categories'),
    path('category-<int:pk>/edit/', EditCategory.as_view(), name='edit_category'),
    path('category-<int:pk>/delete/', DeleteCategory.as_view(), name='delete_category'),
    # -------------------------------------------------------------------------------------
    path('register/', RegistrationUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('user-<int:pk>/profile/', UserProfile.as_view(), name='user_profile'),
    # -------------------------------------------------------------------------------------
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:pk>/add-to-cart/', CartAddView.as_view(), name='add_to_cart'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='remove_for_cart'),
    path('cart/<int:pk>/one-delete/', CartDeleteOneView.as_view(), name='remove_one_for_cart'),
    path('order/create/', OrderCreate.as_view(), name='order_create')
]
