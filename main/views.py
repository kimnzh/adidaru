from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from main.models import Product, Cart, CartItem
from main.forms import ProductForm, CustomUserCreationForm, CustomAuthenticationForm
import datetime

@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    total_items = cart.items.count()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'cart_total': total_items})
    
    messages.success(request, f'Added {product.name} to your cart.')
    return redirect('main:home')

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
@require_POST
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})

    messages.success(request, 'Item removed from cart.')
    return redirect('main:cart')


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
            messages.success(request, f'Welcome back, {user.username}!')
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
    messages.success(request, "You have been successfully logged out.")
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
    product = get_object_or_404(Product, pk=product_id)

    if not product:
      return render(request, 'store/error.html', {'message': 'Product not found.'})

    context = {
        'product': product,
        'product_id': product_id
    }
    return render(request, 'store/product_detail.html', context)

def cart(request):
    """
    View for the shopping cart page.
    This is a placeholder and doesn't have cart logic yet.
    """
    mock_cart_items = [
        # {'product': PRODUCTS[0], 'quantity': 1},
        # {'product': PRODUCTS[2], 'quantity': 2},
    ]
    total_price = sum(item['product'].price * item['quantity'] for item in mock_cart_items)
    context = {
        'cart_items': mock_cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url='/login')
def checkout(request):
    """
    View for the checkout page.
    """
    return render(request, 'store/checkout.html')

@login_required(login_url='/login')
@require_POST
def add_product(request):
    """
    To add new product to the catalogue via AJAX.
    """
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({'status': 'success'}, status=201)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid form data', 'errors': form.errors}, status=400)

@login_required(login_url='/login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user and request.user != product.user:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this product.'}, status=403)
        messages.error(request, 'You are not authorized to delete this product.')
        return HttpResponseRedirect(reverse('main:home'))

    product.delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully!'})
    
    messages.success(request, 'Product deleted successfully!')
    return HttpResponseRedirect(reverse('main:home'))

@login_required(login_url='/login')
@require_POST
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user and request.user != product.user:
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to edit this product.'}, status=403)

    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid form data', 'errors': form.errors}, status=400)

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
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None
            
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

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
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

