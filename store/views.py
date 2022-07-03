from django.shortcuts import render
from .models import *

# Create your views here.


def store(request):
    categories = Category.objects.all()[:4]
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'store/store.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def product_view(request, pk):
    product = Product.objects.prefetch_related('color').prefetch_related('size').get(id=pk)
    context = {'product': product}
    return render(request, 'store/product-view.html',context)
