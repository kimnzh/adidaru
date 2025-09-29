from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Product
from main.forms import ProductForm, CustomUserCreationForm, CustomAuthenticationForm
import datetime

def register(request):
    """
    View for the register page.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'store/register.html', context)

def login_user(request):
    """
    Views for user login
    """
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = CustomAuthenticationForm(request)
    context = {'form': form}
    return render(request, 'store/login.html', context)

@login_required(login_url='/login')
def logout_user(request):
    """
    Views for user logout
    """
    logout(request)
    response = redirect('main:login')
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

@login_required(login_url='/login')
def home(request):
    """
    View for the home page, displaying featured products and a list of all products.
    """
    featured_products = Product.objects.filter(is_featured=True)
    all_products = Product.objects.all()
    context = {
        'featured_products': featured_products,
        'all_products': all_products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, 'store/home.html', context)

@login_required(login_url='/login')
def product_detail(request, product_id):
    """
    View for a single product's detail page.
    """
    product = Product.objects.get(pk=product_id)

    if not product:
      return render(request, 'store/error.html', {'message': 'Product not found.'})

    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)

# def cart(request):
#     """
#     View for the shopping cart page.
#     This is a placeholder and doesn't have cart logic yet.
#     """
#     mock_cart_items = [
#         {'product': PRODUCTS[0], 'quantity': 1},
#         {'product': PRODUCTS[2], 'quantity': 2},
#     ]
#     total_price = sum(item['product'].price * item['quantity'] for item in mock_cart_items)
#     context = {
#         'cart_items': mock_cart_items,
#         'total_price': total_price,
#     }
#     return render(request, 'store/cart.html', context)

@login_required(login_url='/login')
def checkout(request):
    """
    View for the checkout page.
    """
    return render(request, 'store/checkout.html')

@login_required(login_url='/login')
def add_product(request):
    """
    To add new product to the catalogue.
    """
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("main:home")
    
    context = {'form': form}
    return render(request, "store/add_product.html", context)

@login_required(login_url='/login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if not product.user or request.user == product.user:
        product.delete()
        messages.success(request, 'Product deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this product.')
    return HttpResponseRedirect(reverse('main:home'))

@login_required(login_url='/login')
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if not product.user or request.user == product.user:
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:home')

        context = {
            'form': form
        }
        
        return render(request, "store/edit_product.html", context)
    else:
        messages.error(request, 'You are not authorized to edit this product.')
    return HttpResponseRedirect(reverse('main:home'))

# @login_required(login_url="/login")
# def  

def show_xml(request):
    """
    To show Product data in XML.
    """
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    """
    To show Product data in JSON.
    """
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    """
    To show Product data in XML by ID.
    """
    product_item = Product.objects.get(pk=product_id)
    xml_data = serializers.serialize("xml", [product_item])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, product_id):
    """
    To show Product data in JSON by ID.
    """
    product_item = Product.objects.get(pk=product_id)
    json_data = serializers.serialize("json", [product_item])
    return HttpResponse(json_data, content_type="application/json")

