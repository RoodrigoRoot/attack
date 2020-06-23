from django.shortcuts import render
from django.views import View
from .models import Card
# Create your views here.

class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        cards_web = Card.objects.filter(type="w")
        cards_mobile = Card.objects.filter(type="m")
        return render(request, 'core/index.html', locals())
