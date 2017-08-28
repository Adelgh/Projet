from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.response import Response

from serializers import ProduitCreateUpdateSerializer, ProduitListSerializer
from produit.models import Produit


class ProduitCreateAPIView(CreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitCreateUpdateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        buser = user
        shop = Produit.objects.filter(boutique=buser.id)
        serializer.save(shop=Produit[0])


class ProduitListAPIView(ListAPIView):
    def get(self, request, format=None):
        # queryset = self.filter_queryset(self.get_queryset())

        # serializer = self.get_serializer(queryset, many=True)

        produits = Produit.objects.all()

        serializer = ProduitListSerializer(produits, many=True)

        serializer_data = serializer.data

        custom_data = {'produits': serializer_data}

        return Response(custom_data)