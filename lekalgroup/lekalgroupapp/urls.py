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
        ProductListView.as_view(), 
        name='product-list'
    ),
    path(
        'product/<int:product_id>/', 
        ProdcuctDetailView.as_view(), 
        name='product-detail'
    ),

]