from django.shortcuts import render, redirect
from Bakery import models
from django.views import View

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        print(customer)
        cart = request.session.get('cart')
        products = models.Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = models.Order(customer=models.Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            
        request.session['cart'] = {}
        return redirect('Bakery-cart')
