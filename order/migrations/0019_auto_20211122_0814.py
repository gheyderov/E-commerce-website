# Generated by Django 3.2.6 on 2021-11-22 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20211121_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.basket'),
        ),
    ]
