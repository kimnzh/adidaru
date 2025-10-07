from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('product/<uuid:product_id>/', product_detail, name='product_detail'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/<uuid:product_id>/', edit_product, name='edit_product'),
    path('product/delete/<uuid:product_id>/', delete_product, name='delete_product'),
    path('cart/', view_cart, name='cart'),
    path('add-to-cart/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id')
]