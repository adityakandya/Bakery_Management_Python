from django.shortcuts import render, redirect
from Bakery import models
from django.views import View
from django.db.models import F
from django.core.mail import send_mail
from django.contrib import messages

import datetime


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        email = request.session.get('customer_email')
        cart = request.session.get('cart')
        products = models.Product.get_products_by_id(list(cart.keys()))
        order_str = '\n\n'
        total = 0
        a = datetime.datetime.now().time()
        for i in models.Available_hrs.get_all():
            b = (i.Opening_time)
            c = (i.Closing_time)
        if b < a < c:
           
        
            for product in products:
                order = models.Order(customer=models.Customer(id=customer),
                            email=email,
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                models.Product.objects.filter(name=product).update(quantity=F('quantity')-int(cart.get(str(product.id))))
                order.save()
                quantity = cart.get(str(product.id))
                total+=(product.price*int(quantity))
                order_str+=(str(product)+' : '+str(quantity) + '\n')
            
            order_str+=('\nTotal = ' + str(total) + '\n\nThank You for your purchase\n\nBakery')
            send_mail(
                'Purchase Info',
                f'You have purchased these items from our shop - {order_str}',
                'bakerymailpython@gmail.com',
                [email],
                fail_silently=False,)
            request.session['cart'] = {}
            return redirect('Bakery-cart')
        else:
            messages.success(request, 'Shop is Closed!')
            return redirect('Bakery-cart')
        
