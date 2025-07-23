from django.urls import path
from .views import *


urlpatterns = [
    path(
        '', 
        HomePageView.as_view(), 
        name='home-page'
    ),
    path(
        'about/', 
        AboutPageView.as_view(), 
        name='about-page'
    ),
    path(
        'products/', 
        ProductPageView.as_view(), 
        name='product-list'
    ),
    path(
        'product/<slug:product_slug>/', 
        ProductDetailView.as_view(), 
        name='product-detail'
    ),
    path(
        'categories/', 
        CategoryListView.as_view(), 
        name='category-list'
    ),
    path(
        'products/category/<int:category_id>/',
        ProductListByCategoryView.as_view(),
        name='product-by-category'
    ),

]