# Generated by Django 3.2.9 on 2021-11-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Cakes', 'Cakes'), ('Pastry', 'Pastry'), ('Shakes', 'Shakes'), ('Cookies', 'Cookies')], max_length=50, null=True)),
            ],
        ),
    ]
