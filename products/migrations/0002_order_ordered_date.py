# Generated by Django 2.2.14 on 2020-07-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]
