# Generated by Django 3.2.6 on 2021-11-22 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
    ]
