from django.db import models
import datetime


class Available_hrs(models.Model):
    Opening_time = models.TimeField(null=True)
    Closing_time = models.TimeField(null=True)

    @staticmethod
    def get_all():
        return Available_hrs.objects.all()


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
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
    	return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
    	       return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
    @staticmethod
    def get_quantity_by_productid(product_id):
        return Product.objects.get(id=product_id).quantity

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    token = models.CharField(max_length=6, null=True)
    verified = models.BooleanField(default=False)

    def register(self):
        self.save()

    def isExists(self):
        if(Customer.objects.filter(email=self.email)):
            return True
        else:
            return False

    @staticmethod
    def get_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_by_token(token):
        try:
            return Customer.objects.get(token=token)
        except:
            return False

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=15,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_email):
        return Order.objects.filter(email=customer_email).order_by('date')[::-1]
