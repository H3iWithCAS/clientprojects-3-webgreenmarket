# Generated by Django 5.0 on 2024-12-20 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]