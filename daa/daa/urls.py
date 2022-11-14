from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index ,name="index"),   
    path('index/selection', views.ABOUT ,name="mp"),    
    path('index/ABOUT', views.DATASAVE ,name="rt"),
    path('index/ADDITION', views.ADDITION ,name="AD"),
    path('index/description', views.description ,name="AD"),
]
