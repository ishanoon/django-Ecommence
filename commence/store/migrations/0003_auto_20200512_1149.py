# Generated by Django 3.0.5 on 2020-05-12 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
