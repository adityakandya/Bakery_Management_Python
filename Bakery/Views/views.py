from django.shortcuts import render, redirect
from Bakery import models
from django.views import View
from Bakery.models import Product, Order, Customer

class order_history(View):
	def get(self, request):
		customer=request.session.get('customer_email')
		orders=Order.get_orders_by_customer(customer)
		return render(request,'Bakery/order_history.html',{'orders': orders})

def place_order(request):
	return render(request,'Bakery/place_order.html')

class profile(View):
	def get(self,request):
		customeremail=request.session.get('customer_email')
		customer=Customer.get_by_email(customeremail)
		return render(request, 'Bakery/profile.html', {'customer':customer})

def logout(request):
	request.session.clear()
	return redirect('Bakery-login')

class Index(View):
	def post(self,request):

		product = request.POST.get('product')
		limit = Product.get_quantity_by_productid(product)
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

		return redirect('Bakery-index')
	def get(self,request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}

		products = None

		categories = models.Category.get_all_categories()
		categoryID = request.GET.get('category')
		if categoryID:
			products = models.Product.get_all_products_by_categoryid(categoryID)
		else:
			products = models.Product.get_all_products()
		data = {'products':products,'categories':categories}
		return render(request, 'Bakery/index.html', data)
