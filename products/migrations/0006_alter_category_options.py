# Generated by Django 3.2.23 on 2024-01-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_image_url_product_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
