# Generated by Django 3.0.3 on 2020-07-02 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_customer',
        ),
    ]
