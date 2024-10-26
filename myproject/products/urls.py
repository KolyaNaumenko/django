from django.urls import path
from .views import product_view

urlpatterns = [
    path('products/<int:productId>/', product_view),
]
