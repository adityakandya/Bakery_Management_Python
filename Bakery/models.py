from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

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

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
    	       return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
