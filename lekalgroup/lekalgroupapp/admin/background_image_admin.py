from django.contrib import admin

from lekalgroupapp.models import BackgroundImage


@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)