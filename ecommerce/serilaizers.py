from rest_framework import serializers
from . models import *


#model serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=['product_name','product_id','price','discount','product_description']