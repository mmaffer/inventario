# stockwise_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Añadimos las URLs de nuestra app de inventario bajo el prefijo 'api/'
    path('api/', include('inventory.urls')),
]