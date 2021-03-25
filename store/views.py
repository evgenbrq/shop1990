from rest_framework.viewsets import ModelViewSet

from store.models import Product
from store.serializers import ProductSerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

