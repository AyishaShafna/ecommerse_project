from django.db import models
from seller.models import Products
from common_app.models import Customer


# Create your models here.
# class Cart(models.Model):
#     product = models.ForeignKey(Products,on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
#     qunatity = models.BigIntegerField()

# class Meta:
#     db_table = 'cart'