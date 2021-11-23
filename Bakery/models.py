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
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all_products():
    	return Product.objects.all()

