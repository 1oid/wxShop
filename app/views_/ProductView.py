from rest_framework import mixins, viewsets, generics, status
from app.serializers.productSerializer import ProductSerializer
from app.models_.Product import Product


class ProductListView(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        return []

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializer
