# Generated by Django 3.2.6 on 2021-11-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20211114_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]