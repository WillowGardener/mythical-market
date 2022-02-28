from django.urls import path
from . import views

app_name = 'storefront_app'

urlpatterns = [
    path('', views.shop,name='shop'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout,name="checkout"),
    path('create-checkout-session/<int:pk>', views.CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('cancel/', views.CancelView.as_view(), name="cancel-view"),
    path('success/', views.SuccessView.as_view(), name="success-view"),
]
