from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View


from lekalgroupapp.models import (
    Product,
    BackgroundImage,
)

__all__ = [
    'HomePageView',
    'AboutPageView',
    'ProductPageView',
    'ProdcuctDetailView'
]

class HomePageView(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        return render(request, 'index.html', {'background_images': background_images})


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html',)


class ProductPageView(View):
    def get(self, request):
        return render(request, 'product.html')


class ProdcuctDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product-detail.html', {'product': product})
    
