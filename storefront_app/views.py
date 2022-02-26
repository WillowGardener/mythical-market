from django.shortcuts import render

from django.shortcuts import render
from .models import *

def shop(request):
    products = Product.objects.all().order_by('price')
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request,'shop.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product': product
    }

    return render(request,'product_detail.html', context)
