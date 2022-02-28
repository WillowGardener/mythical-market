from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from django.views.generic import TemplateView

import stripe

from storefront_project.secrets import stripe_test_key, stripe_secret_key, stripe_public_key
# stripe.api_key = stripe_test_key


def shop(request):
    products = Product.objects.all().order_by('price')
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'stripe_public_key': stripe_public_key
    }

    return render(request,'shop.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
        'stripe_public_key': stripe_public_key
    }

    return render(request,'product_detail.html', context)

def checkout(request):
    

    return render(request,'checkout.html')

class CreateCheckoutSessionView(View):
    def post(self,request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[

                {

                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.title,
                            # 'images': []

                        }

                    },

                    'quantity': 1,

                },

            ],

            metadata={
                "product_id": product.id
            },

            mode='payment',

            success_url=YOUR_DOMAIN + '/success',

            cancel_url=YOUR_DOMAIN + '/cancel',

        )
        return JsonResponse({
            'id': checkout_session.id
        })

    
class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"