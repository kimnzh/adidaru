from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm

def home(request):
    """
    View for the home page, displaying featured products and a list of all products.
    """
    featured_products = Product.objects.filter(is_featured=True)
    all_products = Product.objects.all()
    context = {
        'featured_products': featured_products,
        'all_products': all_products,
    }
    return render(request, 'store/home.html', context)

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

def checkout(request):
    """
    View for the checkout page.
    """
    return render(request, 'store/checkout.html')

def add_product(request):
    """
    To add new product to the catalogue.
    """
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:home")
    
    context = {'form': form}
    return render(request, "store/add_product.html", context)

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
