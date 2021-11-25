from django.shortcuts import render , redirect
from Bakery import models
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = models.Product.get_products_by_id(ids)
        print(products)
        return render(request, 'Bakery/cart.html',{'products':products})

    def post(self,request):
        product = request.POST.get('product')
        limit = models.Product.get_quantity_by_productid(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                elif quantity>=int(limit):
                    cart[product] = limit
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # return render(request, 'Bakery/cart.html',{'products':products})
        return redirect('Bakery-cart')
