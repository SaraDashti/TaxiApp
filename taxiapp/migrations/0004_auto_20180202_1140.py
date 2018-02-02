# Generated by Django 2.0.1 on 2018-02-02 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0003_customer_driver_meal_order_orderdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]