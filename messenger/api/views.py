from rest_framework import status
from rest_framework.generics import (CreateAPIView,DestroyAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView)
from rest_framework.response import Response

from messenger.api.serializers import MessageListSerializer, MessageCreateUpdateSerializer
from messenger.models import Message


class MessageListAPIView(ListAPIView):
    def get(self, request, format=None):

        queryset = Message.objects.all()

        serializer = MessageListSerializer(queryset, many=True)

        serializer_data = serializer.data

        custom_data = {'message': serializer_data}

        return Response(custom_data)


class MessageCreateAPIView(CreateAPIView):
   serializer_class = MessageCreateUpdateSerializer
   def post(self,request):
       serializer = MessageCreateUpdateSerializer(data=request.data)

       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)

       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
