# Generated by Django 2.2 on 2022-08-28 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='items',
        ),
    ]
