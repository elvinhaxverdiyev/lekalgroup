from django.shortcuts import render
from django.views import View

from lekalgroupapp.models.background_image import BackgroundImage

__all__ = [
    'Home',
    'About'
]

class Home(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        return render(request, 'index.html', {'background_images': background_images})


class About(View):
    def get(self, request):
        return render(request, 'about.html',)

