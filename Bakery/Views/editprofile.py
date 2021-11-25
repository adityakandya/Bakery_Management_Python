from django.shortcuts import render, redirect
from Bakery import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class EditProfile(View):
	def get(self, request):
		email = request.session.get('customer_email')
		print(email)
		customer = models.Customer.get_by_email(email)
		first_name = customer.first_name
		last_name = customer.last_name
		email = customer.email
		phone = customer.phone
		value = {
	            'first_name': first_name,
	            'last_name': last_name,
	            'phone': phone,
	            'email': email
	        }
		return render(request, 'Bakery/edit_profile.html', {'values':value})

	def post(self, request):
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')

		customer = models.Customer.get_by_email(email)

		customer.first_name = first_name
		customer.last_name = last_name
		customer.email = email
		customer.phone = phone
		customer.save()

		return redirect('Bakery-profile')


