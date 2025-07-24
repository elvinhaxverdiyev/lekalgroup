from django.contrib import admin
from django.utils.html import format_html

from lekalgroupapp.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'logo_preview')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" style="object-fit:contain;" />', obj.logo.url)
        return ""
    