from django.urls import path
from .views import HomePageView , AboutPageView, HomepageView, MainPageView

urlpatterns = [
    path('about/', HomePageView.as_view(),name='umid'),
    path('', AboutPageView.as_view(), name='about'),
    path('kun.uz/', HomepageView.as_view(), name='home'),
    path('asosiy/', MainPageView.as_view(), name='main'),
]