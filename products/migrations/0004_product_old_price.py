# Generated by Django 3.2.6 on 2021-11-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
