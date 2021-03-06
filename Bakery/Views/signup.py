from django.shortcuts import render, redirect
from Bakery import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
import re

def validate_password(pwd):
	reg = "^(?=.*[A-Z])(?=.*\d)(?=.*[#$&%@])[A-Za-z\d#$&%@]{8,16}$"
	if re.search(reg, pwd):
		return True
	else:
		return False

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
		conf_password = postData.get('confpassword')

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
		elif not validate_password(password):
			error_message = 'Password must be between 8 to 16 char long, should contain 1 Capital letter, 1 Digit and 1 special character.'
		elif password!=conf_password:
			error_message = 'New Password and confirm password not same!'
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

