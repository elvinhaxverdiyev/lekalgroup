from django.contrib import admin

from lekalgroupapp.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name',)
