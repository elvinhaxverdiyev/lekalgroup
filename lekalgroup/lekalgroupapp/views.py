from django.shortcuts import render
from django.views import View

__all__ = [
    'Home',
    'About'
]

class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')
