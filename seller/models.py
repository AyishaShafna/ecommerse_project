from django.db import models
from common_app.models import Seller

# Create your models here.


class Products(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 200)
    product_price = models.FloatField()
    product_no = models.BigIntegerField()
    product_category = models.CharField(max_length = 200)
    product_description = models.CharField(max_length = 500)
    product_stock = models.BigIntegerField()
    product_images = models.ImageField(upload_to = 'products/')

class Meta:
    db_table = 'products_tbl'


