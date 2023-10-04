from django.urls import path
from .views import home
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('infos/', views.informacoes, name='informacoes'),
    path('historico/', views.historico, name='historico'),

]