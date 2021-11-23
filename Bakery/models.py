from django.db import models

CATEGORY = (
    ('Cakes', 'Cakes'),
    ('Pastry', 'Pastry'),
    ('Shakes', 'Shakes'),
    ('Cookies', 'Cookies'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    image = models.ImageField(upload_to='uploads/products/', default='default_image.jpeg')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all_products():
    	return Product.objects.all()

