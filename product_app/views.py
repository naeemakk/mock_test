from rest_framework.generics import ListAPIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import *

from product_app.models import*
from product_app.serializers import *


class Signup(APIView):

    def post(self, request):
        serializer = product
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUES)


class productlist(ListAPIView):
    queryset = product.objects.all()
    serializer_class = product

class productDetail(RetrieveAPIView):
    queryset =product.objects.all()
    serializer_class = product
    
class productUpdateDelete(UpdateAPIView,DestroyAPIView):
    queryset=product.objects.all()
    serializer_class=product