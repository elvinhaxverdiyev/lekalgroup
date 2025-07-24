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
        'products/category/<slug:category_slug>/',
        ProductListByCategoryView.as_view(),
        name='product-by-category'
    ),
]