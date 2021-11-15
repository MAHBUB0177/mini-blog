# Generated by Django 3.2.6 on 2021-11-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('Desc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products_Packet_Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=20)),
                ('packet_product_id', models.CharField(blank=True, max_length=20)),
                ('quantity_ratio', models.IntegerField(null=True)),
                ('app_user_id', models.CharField(max_length=20)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
