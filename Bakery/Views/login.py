from django.shortcuts import render, redirect
from Bakery import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from django.contrib import messages

import datetime

class Login(View):
	def get(self, request):
		return render(request, 'Bakery/login.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')

		customer = models.Customer.get_by_email(email)

		if customer:
			if check_password(password, customer.password):
				request.session['customer_id']=customer.id
				request.session['customer_email']=customer.email
				a = datetime.datetime.now().time()
				for i in models.Available_hrs.get_all():
					b = (i.Opening_time)
					c = (i.Closing_time)
				if b < a < c:
					return redirect('Bakery-index')
				else:
					messages.success(request, 'Shop is Closed!')
					return redirect('Bakery-login')
			else:
				error_message = 'Email or Password Invalid'
		else:
			error_message = 'Email or Password Invalid'
		return render(request, 'Bakery/login.html', {'error':error_message})
