"""The modularisation urls.py file, realted to the app itself"""

from django.urls import path

from . import views

urlpatterns= [
    path('home', views.home),
    path('home', views.home)
]