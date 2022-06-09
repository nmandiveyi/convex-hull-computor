from django.views.generic import ListView
from django.shortcuts import render

class Home(ListView):
    template_name: str = "index.html"
    
    def get_queryset(self):
        pass

