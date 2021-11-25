from django.shortcuts import render, redirect
from Bakery import models
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class ChangePassword(View):
	def get(self, request):
		return render(request, 'Bakery/change_password.html')

	def post(self, request):
		old_password = request.POST.get('oldpassword')
		new_password = request.POST.get('newpassword')

		email = request.session.get('customer_email')
		customer = models.Customer.get_by_email(email)

		if check_password(old_password, customer.password):
			customer.password = make_password(new_password)
			customer.save()
			return redirect('Bakery-profile')
		else:
			return render(request, 'Bakery/change_password.html', {'error':'Old Password is incorrect!'})

		


