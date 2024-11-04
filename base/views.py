from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from .serializers import ProductSerializer




def index(req):
    return JsonResponse('hello', safe=False)




def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)