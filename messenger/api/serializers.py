from rest_framework.serializers import ModelSerializer

from messenger.models import Message


class MessageListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['from_user','conversation','message','is_read']




class MessageCreateUpdateSerializer(ModelSerializer):
    class Meta :
        model = Message
        fields = ['from_user','user','conversation','message']
