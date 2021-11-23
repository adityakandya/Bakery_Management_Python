from django.shortcuts import render
from . import models
# Create your views here.



def index(request):
	products = models.Product.get_all_products()
	return render(request, 'Bakery/index.html', {'products':products})
