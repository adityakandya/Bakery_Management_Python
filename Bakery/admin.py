from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer

class AdminProduct(admin.ModelAdmin):
	list_display = ['name','quantity','price', 'category']

class AdminCategory(admin.ModelAdmin):
	list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
	list_display = ['first_name']

# Register your models here.

admin.site.site_header = 'Admin Site'

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
# admin.site.register(Order)
