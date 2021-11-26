from django.shortcuts import render, redirect
from Bakery import models
from django.views import View
from Bakery.models import Product, Order, Customer

class order_history(View):
	def get(self, request):
		customer=request.session.get('customer_email')
		print(customer)
		orders=Order.get_orders_by_customer(customer)
		print('orders', orders)
		return render(request,'Bakery/order_history.html',{'orders': orders})

def place_order(request):
	return render(request,'Bakery/place_order.html')

class profile(View):
	def get(self,request):
		customeremail=request.session.get('customer_email')
		customer=Customer.get_by_email(customeremail)
		return render(request, 'Bakery/profile.html', {'customer':customer})

class editprofile(View):
	def get(self,request):
		customeremail=request.session.get('customer_email')
		customer=Customer.get_by_email(customeremail)
		fields = ['first_name','last_name','phone']
		return render(request, 'Bakery/edit_profile.html',{'customer':customer})
	def post(self,request):
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone = request.POST.get('phone')
		customeremail=request.session.get('customer_email')
		models.Customer.objects.filter(email=customeremail).update(first_name=first_name,last_name=last_name,phone=phone)
		return redirect('Bakery-profile')

def logout(request):
	request.session.clear()
	return redirect('Bakery-login')

class Index(View):

	def post(self,request):
		product = request.POST.get('product')
		limit = Product.get_quantity_by_productid(product)
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		print("limit is ", limit)
		categories = models.Category.get_all_categories()
		categoryID = request.GET.get('category')
		if categoryID:
			products = models.Product.get_all_products_by_categoryid(categoryID)
		else:
			products = models.Product.get_all_products()


		if cart:
			if limit == 0:


				data = {'products':products,'categories':categories}
				# return redirect('Bakery-index')
				return render(request,'Bakery/index.html',data)
			else:

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
				request.session['cart'] = cart
				return redirect('Bakery-index')
		else:

			cart = {}
			if limit != 0 :
				cart[product] = 1
				request.session['cart'] = cart
				return redirect('Bakery-index')
			else:

				data = {'products':products,'categories':categories}
				return render(request,'Bakery/index.html',data)



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
