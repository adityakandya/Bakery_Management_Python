from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='uploads/products/', default='default_image.jpeg')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all_products():
    	return Product.objects.all()

