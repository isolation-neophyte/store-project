from django.shortcuts import render
from products import models

# Create your views here.

def index(request):
    context = {
        "title": "Store"
    }
    return render(request, "products/index.html", context=context)

def products(request):
    context = {
        "title": "Store - Каталог",
        "categories": models.ProductCategory.objects.all(),
        "products": models.Product.objects.all(),
    }
    return render(request, "products/products.html", context=context)