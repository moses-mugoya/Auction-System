# Generated by Django 2.0.6 on 2018-08-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20180819_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='security_code',
            field=models.IntegerField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='credit_number',
            field=models.IntegerField(max_length=16),
        ),
    ]