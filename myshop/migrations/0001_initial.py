# Generated by Django 5.0.6 on 2024-05-26 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('client_reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_desc', models.CharField(max_length=100)),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prod_quant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prod_reg_date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_order', models.FloatField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.client')),
                ('products', models.ManyToManyField(to='myshop.product')),
            ],
        ),
    ]
