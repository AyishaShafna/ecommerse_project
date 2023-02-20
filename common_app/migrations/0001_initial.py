# Generated by Django 4.1.6 on 2023-02-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='customer/')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_address', models.CharField(max_length=500)),
                ('company_mobile', models.BigIntegerField()),
                ('company_email', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(upload_to='seller/')),
                ('bank_name', models.CharField(max_length=300)),
                ('acc_holder', models.CharField(max_length=300)),
                ('acc_no', models.BigIntegerField()),
                ('ifsc_code', models.CharField(max_length=100)),
                ('seller_username', models.CharField(max_length=200)),
                ('seller_password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'seller_details',
            },
        ),
    ]