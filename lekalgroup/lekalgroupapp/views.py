from django.shortcuts import render
from django.views import View


from lekalgroupapp.models import (
    Product,
    BackgroundImage,
)

__all__ = [
    'HomePage',
    'AboutPage',
    'ProductPage',
    'ProdcuctDetail'
]

class HomePage(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        return render(request, 'index.html', {'background_images': background_images})


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html',)


class ProductPage(View):
    def get(self, request):
        return render(request, 'product.html')


class ProdcuctDetail(View):
    def get(self, request, product_id):
        return render(request, 'product-detail.html')
    
