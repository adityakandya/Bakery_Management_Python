from django.shortcuts import render , redirect
from Bakery import models
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = models.Product.get_products_by_id(ids)
        print(products)
        return render(request, 'Bakery/cart.html',{'products':products})
