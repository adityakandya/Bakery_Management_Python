from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
	categories = models.Category.get_all_categories()
	categoryID = request.GET.get('category')
	if categoryID:
		products = models.Product.get_all_products_by_categoryid(categoryID)
	else:
		products = models.Product.get_all_products()
	data = {'products':products,'categories':categories}
	return render(request, 'Bakery/index.html', data)

def signup(request):
	return render(request, 'Bakery/signup.html')
