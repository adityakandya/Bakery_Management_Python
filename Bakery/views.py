from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

def order_history(request):
	return render(request,'Bakery/order_history.html')

def place_order(request):
	return render(request,'Bakery/place_order.html')

def cart(request):
	return render(request,'Bakery/cart.html')


def index(request):
	categories = models.Category.get_all_categories()
	categoryID = request.GET.get('category')
	if categoryID:
		products = models.Product.get_all_products_by_categoryid(categoryID)
	else:
		products = models.Product.get_all_products()
	data = {'products':products,'categories':categories}
	return render(request, 'Bakery/index.html', data)


class Signup(View):
	def get(self, request):
		return render(request, 'Bakery/signup.html')

	def post(self, request):
		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email= postData.get('email')
		password = postData.get('password')

		value = {
	            'first_name': first_name,
	            'last_name': last_name,
	            'phone': phone,
	            'email': email
	        }

		error_message = None
		customer = models.Customer(first_name = first_name, last_name = last_name,
				phone = phone,email = email,password = password)


		if not customer.first_name:
			error_message = "First Name Required !!"
		elif len(customer.first_name) < 4:
			error_message = 'First Name must be 4 char long or more'
		elif not customer.last_name:
			error_message = 'Last Name Required'
		elif len(customer.last_name) < 4:
			error_message = 'Last Name must be 4 char long or more'
		elif not customer.phone:
			error_message = 'Phone Number required'
		elif len(customer.phone) < 10:
			error_message = 'Phone Number must be 10 char Long'
		elif len(customer.password) < 6:
			error_message = 'Password must be 6 char long'
		elif len(customer.email) < 5:
			error_message = 'Email must be 5 char long'
		elif customer.isExists():
			error_message = 'Email Address Already Registered..'

		if not error_message:
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('Bakery-login')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'Bakery/signup.html', data)

class Login(View):
	def get(self, request):
		return render(request, 'Bakery/login.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		customer = models.Customer.get_by_email(email)
		if customer:
			if check_password(password, customer.password):
				return redirect('Bakery-index')
			else:
				error_message = 'Email or Password Invalid'
		else:
			error_message = 'Email or Password Invalid'
		return render(request, 'Bakery/login.html', {'error':error_message})





	



