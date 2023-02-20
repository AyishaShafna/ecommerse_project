from django.db import models

# Create your models here. (creating tables/relations for database)
class Customer(models.Model):
    customer_name = models.CharField(max_length = 100)   #these are column/attributes in table
    address = models.CharField(max_length = 300)
    mobile = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'customer/')

    class Meta:
        db_table = 'customer'

class Seller(models.Model):
    company_name = models.CharField(max_length = 200)
    company_address = models.CharField(max_length = 500)
    company_mobile = models.BigIntegerField()
    company_email = models.CharField(max_length = 200)
    company_logo = models.ImageField(upload_to = 'seller/')
    bank_name = models.CharField(max_length = 300)
    acc_holder = models.CharField(max_length = 300)
    acc_no = models.BigIntegerField()
    ifsc_code = models.CharField(max_length = 100)
    seller_username = models.CharField(max_length = 200)
    seller_password = models.CharField(max_length = 100)

    class Meta:
        db_table = 'seller_details'


