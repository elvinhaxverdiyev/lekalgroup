from django.contrib import admin

from lekalgroupapp.models.product import Product
from lekalgroupapp.models.product_image import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  
    fields = ('image',)
    verbose_name = "Məhsul şəkli"
    verbose_name_plural = "Məhsul şəkilləri"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]