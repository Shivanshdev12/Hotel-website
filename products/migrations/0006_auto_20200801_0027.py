# Generated by Django 2.2.14 on 2020-07-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200731_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=True),
        ),
    ]
