from django.shortcuts import render
from .models import Product

def home(request):
    featured_products = Product.objects.all()[:4]
    return render(request, 'home.html', {'featured_products': featured_products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tips(request):
    return render(request, 'tips.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products.html', context)