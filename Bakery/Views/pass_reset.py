from django.shortcuts import render, redirect
from Bakery import models
from django.views import View
from django.core.mail import send_mail
from Bakery import models
import random
from django.contrib.auth.hashers import make_password

class PasswordReset(View):
	def get(self, request):
		return render(request, 'Bakery/password_reset.html')

	def post(self, request):
		email = request.POST.get('email')
		token = int(random.random()*1000000)
		customer = models.Customer.get_by_email(email)
		customer.token=token
		customer.save()
		print('Customer token added in DB', customer.token, 'for', customer.email)
		if customer:
			customer.token = token
			send_mail(
		    'Password Reset',
		    f'Enter this token to reset your password - {token}',
		    'bakerymailpython@gmail.com',
		    [email],
		    fail_silently=False,)
			return redirect('password_reset_check')

		else:
			return render(request, 'Bakery/password_reset.html', {'error':'Enter correct Email'})


class PasswordResetCheck(View):
	def get(self, request):
		return render(request, 'Bakery/password_reset_check.html')

	def post(self, request):
		token = request.POST.get('token')
		customer = models.Customer.get_by_token(token)

		
		if customer:
			customer.token = ''
			customer.password = make_password(request.POST.get('password'))
			customer.save()
			return redirect('Bakery-login')
		else:
			return render(request, 'Bakery/password_reset_check.html', {'error':'Token Wrong'})




