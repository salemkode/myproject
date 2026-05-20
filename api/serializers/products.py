from rest_framework import serializers
from products.models import Product
 
class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       # The fields we want to "expose" to the public API
       fields = ['name', 'description', 'price']
       
       # Note: We can also use fields = '__all__' to expose everything