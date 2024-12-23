from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tips/', views.tips, name='tips'),
    path('products/', views.products, name='products'),
]