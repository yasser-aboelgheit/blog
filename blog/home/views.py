from django.views.generic import TemplateView, CreateView
from datetime import datetime

class HomePageView(TemplateView):
    template_name = 'home/home.html'
