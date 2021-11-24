from django.contrib import admin
from .models import Product
from .models import Category


class AdminProduct(admin.ModelAdmin):
	list_display = ['name','quantity','price', 'category']

class AdminCategory(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.

admin.site.site_header = 'Admin Site'

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
# admin.site.register(Order)
