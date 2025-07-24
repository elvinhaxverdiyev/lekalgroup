from django.contrib import admin
from django.utils.html import format_html

from lekalgroupapp.forms import ProductImageInlineFormSet
from lekalgroupapp.models import Product, ProductImage, Category




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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent_category__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
