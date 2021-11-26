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


class ChangePassword(View):
	def get(self, request):
		return render(request, 'Bakery/change_password.html')

	def post(self, request):
		old_password = request.POST.get('oldpassword')
		new_password = request.POST.get('newpassword')
		new_password2 = request.POST.get('newpassword2')

		email = request.session.get('customer_email')
		customer = models.Customer.get_by_email(email)

		if check_password(old_password, customer.password) and new_password==new_password2 and validate_password(new_password):
			customer.password = make_password(new_password)
			customer.save()
			return redirect('Bakery-profile')

		elif not validate_password(new_password):
			return render(request, 'Bakery/change_password.html', {'error':'Password must be between 8 to 16 char long, should contain 1 Capital letter, 1 Digit and 1 special character.'})


		elif new_password!=new_password2:
			return render(request, 'Bakery/change_password.html', {'error':'New Password and confirm password not same!'})


		else:
			return render(request, 'Bakery/change_password.html', {'error':'Old Password is incorrect!'})

		


