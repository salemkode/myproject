from rest_framework.generics import ListCreateAPIView
from products.models import Product
from .serializers.products import ProductSerializer
 
class ProductListCreateAPI(ListCreateAPIView):
   # 1. What data are we looking at?
   queryset = Product.objects.all()
   
   # 2. How should we translate it to JSON?
   serializer_class = ProductSerializer