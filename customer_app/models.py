from django.db import models
from seller.models import Products
from common_app.models Customer


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,on_update=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,on_update=models.CASCADE)