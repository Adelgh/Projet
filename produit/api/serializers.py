from rest_framework.serializers import ModelSerializer

from produit.models import Produit


class ProduitCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['title','descreption','prix','etat','categorie','tags','logo']



class ProduitListSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['title','descreption','prix','etat','categorie','tags','logo']
