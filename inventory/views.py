# inventory/views.py

from rest_framework import viewsets, filters
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# 📚 CRUD básico de Entidad 2 (Categoría)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# 📃 Listado, ➕ Creación, ✏ Edición, ❌ Eliminación y 🔍 Búsqueda de Entidad 1 (Producto)
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    # 🔍 Implementación de búsqueda por filtros
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre'] # Campos por los que se podrá buscar, puedes añadir más