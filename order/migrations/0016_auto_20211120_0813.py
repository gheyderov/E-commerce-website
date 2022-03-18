# Generated by Django 3.2.6 on 2021-11-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_billingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='address_1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address_1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='address_2',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
