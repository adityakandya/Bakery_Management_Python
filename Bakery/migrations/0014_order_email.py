# Generated by Django 3.2.9 on 2021-11-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bakery', '0013_auto_20211125_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='sandramaryjacob27@gmail.com', max_length=254),
        ),
    ]
