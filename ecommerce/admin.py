from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(products)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_id','discount','price','product_description']
