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
    # path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id')
]