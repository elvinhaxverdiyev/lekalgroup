from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View


from lekalgroupapp.models import (
    Product,
    Category,
    BackgroundImage,
)

__all__ = [
    'HomePageView',
    'AboutPageView',
    'ProductPageView',
    'ProductDetailView',
    'ProductListByCategoryView',
    'CategoryListView'
]

class HomePageView(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        popular_products = Product.objects.filter(
            is_active=True, is_popular=True
            ).order_by('-created_at')
        
        return render(request, 'index.html', {
            'popular_products': popular_products,
            'background_images': background_images
            })


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html',)


class ProductPageView(View):
    def get(self, request):
        products = Product.objects.filter(
            is_active=True).order_by('-created_at')
        return render(request, 'product.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, 'product-detail.html', {'product': product})


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'index.html', {'categories': categories})
    

class ProductListByCategoryView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        return render(request, 'product.html', {
            'products': products,
            'category': category
        })
