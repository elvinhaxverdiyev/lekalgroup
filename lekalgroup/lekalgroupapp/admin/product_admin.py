from django.contrib import admin

from lekalgroupapp.models.product import Product
from lekalgroupapp.models.product_image import ProductImage
from lekalgroupapp.forms import ProductImageInlineFormSet 


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]