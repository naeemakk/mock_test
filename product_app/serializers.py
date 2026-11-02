from rest_framework import serializers
from product_app.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['name','description','category','price','stock',]
        read_olny_field=['id','created_at']