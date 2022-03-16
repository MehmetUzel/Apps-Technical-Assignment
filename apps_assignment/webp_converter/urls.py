from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_converter_page, name="get_converter_page"),
    path('convert/', views.convert_image, name= 'convert_image'),

]