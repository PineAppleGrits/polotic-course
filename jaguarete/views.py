from .models import Category, Product, Cart
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, get_list_or_404, get_object_or_404, render
from django.contrib.auth.decorators import permission_required, login_required
from .forms import ProductForm
# Create your views here.


def index(request):
    
    last_three = Product.objects.all().order_by('-id')[:3]
    all_items = Product.objects.all().order_by('-id')[3:]
    all_categories = Category.objects.all()
    user_cart = None
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).exists()
        if not user_cart:
            newCart = Cart(user=request.user)
            newCart.save()
            user_cart = newCart
        else:
            user_cart = Cart.objects.get(user=request.user)
    context = {
        'last_three': last_three,
        'all_items': all_items,
        'all_categories': all_categories,
        'user_cart': user_cart
    }
    return render(request,'jaguarete/index.html', context)

def categoria(request, categoria):
    all_items =  Product.objects.filter(category=categoria)
    category = get_object_or_404(Category, id=categoria)
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
        'category': category,
        'all_items': all_items 
    }
    return render(request,'jaguarete/category.html', context)

def search(request):
    query = request.GET.get('q')
    all_items =  Product.objects.filter(Q(title__icontains=query) | Q(long_description__icontains=query) | Q(price__icontains=query))
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
        'all_items': all_items 
    }
    
    return render(request,'jaguarete/search.html', context)

def product(request, product):
    has = request.user.groups.filter(name="Moderador").exists()
    if has:
        return edit_product(request, product);
    product = get_object_or_404(Product, id=product)
    all_categories = Category.objects.all()
    user_cart = None
    if request.user.is_authenticated:
        user_cart = Cart.objects.get(user=request.user)
    context = {
        'product': product,
        'all_categories': all_categories,
        'user_cart': user_cart
    }
    return render(request,'jaguarete/product.html', context)

@login_required
def add_to_cart(request, product):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        productobj= get_object_or_404(Product, id=product)
        cart.products_list.add(productobj)
        return redirect('/')
    else:
        return redirect('/')


@permission_required('jaguarete.add_product')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'jaguarete/add_product.html',  {'form': form})

@login_required
def cart_list(request):  
    if request.method == 'POST':
        print(request.POST.get('producto'))
    #    query = request.GET.get('q')
    #    all_items =  Product.objects.filter(Q(title__icontains=query) | Q(long_description__icontains=query) | Q(price__icontains=query))
    all_categories = Category.objects.all()
    carrito = Cart.objects.get(user=request.user)
    context ={
    'user_cart': carrito,
    'all_categories': all_categories,

    }
    return render(request, 'jaguarete/carrito.html', context)

@login_required
def del_cart_item(request, product):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        productobj= get_object_or_404(Product, id=product)
        cart.products_list.remove(productobj)
    return redirect('/carrito')

@permission_required('jaguarete.delete_product')
def del_product(request, product):
    if request.method == 'POST':
        Product.objects.get(id=product).delete()
    return redirect('/')

@permission_required('jaguarete.change_product')
def edit_product(request, product):
    instance = get_object_or_404(Product, id=product)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('/')
    return render(request, 'jaguarete/edit_product.html',  {'form': form, 'product': instance})