# Generated by Django 3.2.6 on 2022-02-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_product_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='country_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]