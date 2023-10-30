from django.db import models

# Create your models here.
#models used for ORM
class products(models.Model):
    product_name=models.CharField(max_length=50)
    product_id=models.IntegerField()
    price=models.IntegerField()
    discount=models.IntegerField()
    product_description=models.TextField()

