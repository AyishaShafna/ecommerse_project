from django.db import models

# Create your models here.
class Ecom_Admin(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
class Meta:
    db_table = 'admin_tbl'