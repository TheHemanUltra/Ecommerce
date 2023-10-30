from rest_framework import viewsets
from ecommerce.models import *
from ecommerce.serilaizers import *

#views set to handle user request
class ProductViewSet(viewsets.ModelViewSet):
    queryset=products.objects.all()
    serializer_class=ProductSerializer