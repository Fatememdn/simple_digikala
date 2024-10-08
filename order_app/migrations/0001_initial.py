# Generated by Django 5.1 on 2024-08-18 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('cart_app', '0001_initial'),
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('code', models.CharField(blank=True, help_text='code shouldnt be more than 10 characters', max_length=10, null=True)),
                ('initiated_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.costumer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_status', models.BooleanField(blank=True, null=True)),
                ('date', models.DateField(blank=True, help_text='the time when the order was set first', null=True)),
                ('bill', models.FloatField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.costumer')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cart_app.cart')),
                ('discount_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order_app.discount')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('num', models.IntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(blank=True, help_text='this item is related to which order', null=True, on_delete=django.db.models.deletion.CASCADE, to='order_app.order')),
                ('product', models.ForeignKey(blank=True, help_text='this product', null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
            ],
        ),
    ]
