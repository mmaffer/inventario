# inventory/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet

# Creamos un router
router = DefaultRouter()
# Registramos nuestras vistas con el router
router.register(r'productos', ProductoViewSet) # Entidad 1
router.register(r'categorias', CategoriaViewSet) # Entidad 2

# Las URLs de la API son generadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]