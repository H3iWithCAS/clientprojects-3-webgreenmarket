# Generated by Django 5.0 on 2024-12-20 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegan', '0002_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
