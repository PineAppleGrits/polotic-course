from django.shortcuts import render
from .models import Category, Product, Cart
from django.conf import settings
from django.db.models import Q
# Create your views here.


def index(request):
    last_three = Product.objects.all().order_by('-id')[:3]
    all_items = Product.objects.all().order_by('-id')[3:]
    all_categories = Category.objects.all()
    user_cart = None
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user)[0]
    context = {
        'last_three': last_three,
        'all_items': all_items,
        'all_categories': all_categories,
        'user_cart': user_cart
    }
    return render(request,'jaguarete/index.html', context)

def categoria(request, categoria):
    all_items =  Product.objects.filter(category=categoria)
    category = Category.objects.get(id=categoria)
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
        'category': category,
        'all_items': all_items 
    }
    return render(request,'jaguarete/category.html', context)

def search(request):
    query = request.GET.get('q')
    all_items =  Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query))
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
        'all_items': all_items 
    }
    
    return render(request,'jaguarete/search.html', context)

def product(request, product):
    product = Product.objects.get(id=product)
    all_categories = Category.objects.all()
    user_cart = None
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user)[0]
    context = {
        'product': product,
        'all_categories': all_categories,
        'user_cart': user_cart
    }
    return render(request,'jaguarete/product.html', context)


