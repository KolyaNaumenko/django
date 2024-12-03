"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.core.cache import cache
from django.http import JsonResponse
import time

# Импортируйте ваше представление

from django.urls import path, include
def home(request):
    return HttpResponse("Welcome to the Django Project!")
# Представление для маршрута /get-product/
def get_product_info(request):
    cache_key = 'product_info'
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse({'status': 'from_cache', 'data': cached_data})

    # Симуляция долгого вычисления
    time.sleep(3)
    product_data = {'id': 1, 'name': 'Laptop', 'price': 1200}

    cache.set(cache_key, product_data, timeout=60)  # Кешируем данные на 60 секунд
    return JsonResponse({'status': 'from_db', 'data': product_data})

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('django_prometheus.urls')),
    path('get-product/', get_product_info, name='get-product'),

]
