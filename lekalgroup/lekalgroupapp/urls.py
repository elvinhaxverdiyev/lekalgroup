from django.urls import path
from .views import *


urlpatterns = [
    path(
        '', 
        Home.as_view(), 
        name='home-page'
    ),
    path(
        'about/', 
        About.as_view(), 
        name='about-page'
    ),

]