# Generated by Django 3.1.4 on 2021-12-26 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dashboard',
            new_name='user',
        ),
    ]
