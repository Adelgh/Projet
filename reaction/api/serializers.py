from rest_framework.serializers import ModelSerializer

from reaction.models import Reaction



class ReactionListSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['user','product','type']


class ReactionCreateUpdateSerializer(ModelSerializer):
    class Meta :
        model = Reaction
        fields = ['product','type']
