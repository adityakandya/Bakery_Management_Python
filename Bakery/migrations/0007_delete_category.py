# Generated by Django 3.2.9 on 2021-11-24 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bakery', '0006_remove_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
