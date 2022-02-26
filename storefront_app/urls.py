from django.urls import path
from . import views

app_name = 'storefront_app'

urlpatterns = [
    path('', views.shop,name='shop'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail')
]