# Generated by Django 2.0.6 on 2018-08-18 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20180818_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='account.Person'),
        ),
    ]
