from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def product_view(request, productId):
    return JsonResponse({"id": str(productId), "name": f"{productId} name"})
