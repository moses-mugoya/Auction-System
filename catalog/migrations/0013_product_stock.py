# Generated by Django 2.0.6 on 2018-08-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=30),
        ),
    ]