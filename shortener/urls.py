from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='shortener.index'),
    re_path(r'^[a-zA-Z0-9]{1,}$', views.lengthen, name="shortener.lengthen"),
    path('shortener/', views.shorten, name='shortener.shorten')
]   