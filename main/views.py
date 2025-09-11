from django.shortcuts import render
from main.models import PRODUCTS

def home(request):
    """
    View for the home page, displaying featured products and a list of all products.
    """
    featured_products = [p for p in PRODUCTS if p.is_featured]
    all_products = PRODUCTS
    context = {
        'featured_products': featured_products,
        'all_products': all_products,
    }
    return render(request, 'store/home.html', context)

def product_detail(request, product_id):
    """
    View for a single product's detail page.
    """
    # In a real app: product = get_object_or_404(Product, id=product_id)
    product = None
    for p in PRODUCTS:
        if str(p.id) == str(product_id):
            product = p
    if not product:
      # A simple way to handle not found without raising Http404 for this example
      return render(request, 'store/error.html', {'message': 'Product not found.'})

    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)

def cart(request):
    """
    View for the shopping cart page.
    This is a placeholder and doesn't have cart logic yet.
    """
    # For demonstration, we'll add a few products to a mock cart
    mock_cart_items = [
        {'product': PRODUCTS[0], 'quantity': 1},
        {'product': PRODUCTS[2], 'quantity': 2},
    ]
    total_price = sum(item['product'].price * item['quantity'] for item in mock_cart_items)
    context = {
        'cart_items': mock_cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    """
    View for the checkout page.
    This is a placeholder.
    """
    return render(request, 'store/checkout.html')

