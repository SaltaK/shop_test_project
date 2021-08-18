from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def test(request):
    data = {
        'text': 'Hello world'
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data)


@api_view(['GET'])
def category_item_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'message': 'category not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(category).data
    return Response(data=data)


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_item_view(request, id):
    products = Product.objects.get(id=id)
    data = ProductSerializer(products).data
    return Response(data=data)