from django.shortcuts import render, redirect
from Bakery import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Login(View):
	def get(self, request):
		return render(request, 'Bakery/login.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(email,password)

		customer = models.Customer.get_by_email(email)
		print(customer)
		if customer:
			if check_password(password, customer.password):
				request.session['customer_id']=customer.id
				request.session['customer_email']=customer.email
				return redirect('Bakery-index')
			else:
				error_message = 'Email or Password Invalid'
		else:
			error_message = 'Email or Password Invalid'
		return render(request, 'Bakery/login.html', {'error':error_message})
