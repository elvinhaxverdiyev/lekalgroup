from django.contrib import admin
from django.utils.html import format_html

from lekalgroupapp.forms import ProductImageInlineFormSet

from lekalgroupapp.models.product import Product
from PIL import Image
from lekalgroupapp.models.product_image import ProductImage



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet
    extra = 1
    readonly_fields = ['preview']  
    fields = ['image', 'preview']  

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover;" />', obj.image.url)
        return "-"
    
    preview.short_description = "Şəkil Önizləmə"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]