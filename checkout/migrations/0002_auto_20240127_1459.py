# Generated by Django 3.2.23 on 2024-01-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_has_sizes'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderLlineItem',
            new_name='OrderLineItem',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]