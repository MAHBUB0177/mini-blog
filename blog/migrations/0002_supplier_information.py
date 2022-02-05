# Generated by Django 3.2.6 on 2022-01-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier_Information',
            fields=[
                ('supp_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('branch_code', models.IntegerField(blank=True)),
                ('supp_name', models.CharField(max_length=100)),
                ('proprietor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('account_number', models.CharField(blank=True, max_length=20, null=True)),
                ('supp_address', models.CharField(blank=True, max_length=300, null=True)),
                ('supp_mobile', models.CharField(max_length=20, null=True)),
                ('supp_email', models.CharField(blank=True, max_length=100, null=True)),
                ('supp_web', models.CharField(blank=True, max_length=100, null=True)),
                ('supp_key_person', models.CharField(blank=True, max_length=100, null=True)),
                ('supp_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('app_user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]