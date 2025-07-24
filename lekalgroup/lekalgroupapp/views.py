from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View


from lekalgroupapp.models import (
    Product,
    Category,
    Partner,
    BackgroundImage,
)

__all__ = [
    'HomePageView',
    'AboutPageView',
    'ProductPageView',
    'ProductDetailView',
    'ProductListByCategoryView',
]

class HomePageView(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        partners = Partner.objects.filter(is_active=True)
        popular_products = Product.objects.filter(
            is_active=True, is_popular=True
            ).order_by('-created_at')
        categories = Category.objects.filter(parent_category=None)

        return render(request, 'index.html', {
            'background_images': background_images,
            'popular_products': popular_products,
            'partners': partners,
            'categories': categories
            })


class AboutPageView(View):
    def get(self, request):
        categories = Category.objects.filter(parent_category=None)
        return render(request, 'about.html',{
            'categories': categories
        })


class ProductPageView(View):
    def get(self, request):
        products = Product.objects.filter(
            is_active=True).order_by('-created_at')
        categories = Category.objects.filter(parent_category=None)

        return render(request, 'product.html', {
            'products': products,
            'categories': categories
            })


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        categories = Category.objects.filter(parent_category=None)

        return render(request, 'product-detail.html', {
            'product': product,
            'categories': categories
            })


class ProductListByCategoryView(View):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        categories = Category.objects.filter(parent_category=None)
        return render(request, 'product.html', {
            'products': products,
            'category': category,
            'categories': categories
        })
