from django.urls import path
from .views import *


urlpatterns = [
    path(
        '', 
        HomePage.as_view(), 
        name='home-page'
    ),
    path(
        'about/', 
        AboutPage.as_view(), 
        name='about-page'
    ),
    path(
        'products/', 
        AboutPage.as_view(), 
        name='product-list'
    ),
    path(
        'product/<int:product_id>/', 
        AboutPage.as_view(), 
        name='product-detail'
    ),

]