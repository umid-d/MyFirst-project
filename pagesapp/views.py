from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'umid.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomepageView(TemplateView):
    template_name = 'home.html'

class MainPageView(TemplateView):
    template_name= 'main.html'


