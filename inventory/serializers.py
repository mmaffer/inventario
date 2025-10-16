# inventory/serializers.py

from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' # Incluye todos los campos del modelo

class ProductoSerializer(serializers.ModelSerializer):
    # ✨ Punto Extra: Personalizamos la respuesta para mostrar el nombre
    # de la categoría en lugar de solo su ID.
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        # Definimos los campos que queremos mostrar en la API
        fields = ['id', 'nombre', 'cantidad', 'precio', 'categoria', 'categoria_nombre']
        # 'categoria' será un campo de escritura (para enviar el ID)
        # 'categoria_nombre' será un campo de solo lectura (para mostrar el nombre)