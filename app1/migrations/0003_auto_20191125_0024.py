# Generated by Django 2.2.7 on 2019-11-24 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_orderitem_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='amont',
            new_name='amount',
        ),
    ]
