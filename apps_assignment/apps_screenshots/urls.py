from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.random_match, name="random_match"),
    path('screenshots/', views.get_screenshot, name= 'get_screenshots'),
    path('randomscreenshot/', views.get_random_screenshots, name='get_random_screenshots'),

]