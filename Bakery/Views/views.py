from django.shortcuts import render, redirect
from Bakery import models

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



