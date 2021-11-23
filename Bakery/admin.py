from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_header = 'Admin Site'

admin.site.register(Product)
# admin.site.register(Order)
