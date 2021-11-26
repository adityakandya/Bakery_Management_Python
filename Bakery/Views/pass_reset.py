from django.shortcuts import render, redirect
from Bakery import models
from django.views import View
from django.core.mail import send_mail
from Bakery import models
import random
from django.contrib.auth.hashers import make_password


def gen_token():
	 a = [str(int(random.random()*10)) for i in range(6)]
	 return(''.join(a))


class PasswordReset(View):
	def get(self, request):
		return render(request, 'Bakery/password_reset.html')

	def post(self, request):
		email = request.POST.get('email')
		token = gen_token()
		customer = models.Customer.get_by_email(email)
		if customer:
			customer.token=token
			customer.save()
			print('Customer token added in DB', customer.token, 'for', customer.email)
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
		new_password = request.POST.get('password')
		new_password2 = request.POST.get('newpassword2')

		
		if customer and new_password==new_password2:
			customer.token = ''
			customer.password = make_password(new_password)
			customer.save()
			return redirect('Bakery-login')

		elif new_password!=new_password2:
			return render(request, 'Bakery/password_reset_check.html', {'error':'New Password and confirm password not same!'})

		else:
			return render(request, 'Bakery/password_reset_check.html', {'error':'Token Wrong'})


class VerifyUser(View):
	def get(self, request):
		return render(request, 'Bakery/verify_user.html')

	def post(self, request):
		email = request.session.get('customer_email')
		token = gen_token()
		customer = models.Customer.get_by_email(email)
		customer.token=token
		customer.save()
		print('Customer token added in DB', customer.token, 'for', customer.email)
		if customer:
			customer.token = token
			send_mail(
		    'Email Verification',
		    f'Enter this token to Verify your Email - {token}',
		    'bakerymailpython@gmail.com',
		    [email],
		    fail_silently=False,)
			return redirect('verify_check')

		else:
			return render(request, 'Bakery/verify_user.html', {'error':'Enter correct Email'})


class VerifyCheck(View):
	def get(self, request):
		return render(request, 'Bakery/verify_check.html')

	def post(self, request):
		token = request.POST.get('token')
		customer = models.Customer.get_by_token(token)

		
		if customer:
			customer.token = ''
			customer.verified = True
			customer.save()
			return redirect('Bakery-index')
		else:
			return render(request, 'Bakery/verify_check.html', {'error':'Token Wrong'})

