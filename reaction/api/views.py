from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.response import Response

from serializers import ReactionListSerializer, ReactionCreateUpdateSerializer
from reaction.models import Reaction






class ReactionListAPIView(ListAPIView):
    def get(self, request, format=None):
        # queryset = self.filter_queryset(self.get_queryset())

        # serializer = self.get_serializer(queryset, many=True)

        reactions = Reaction.objects.all()

        serializer = ReactionListSerializer(reactions, many=True)

        serializer_data = serializer.data

        custom_data = {'reactions': serializer_data}

        return Response(custom_data)


class ReactionCreateAPIView(CreateAPIView):
   serializer_class = ReactionCreateUpdateSerializer

   def post(self, request):
       serializer = ReactionCreateUpdateSerializer(data=request.data)
       user = request.user
       if serializer.is_valid():
           try:
               reaction = Reaction.objects.get(user=request.user,product=serializer.validated_data['product'])
               if reaction.type == serializer.validated_data['type']:
                   reaction.delete()

                   return Response(serializer.data, status=status.HTTP_201_CREATED)
               else:
                   serializer.save(user=request.user)
                   return Response(serializer.data, status=status.HTTP_201_CREATED)
           except Reaction.DoesNotExist:
               serializer.save(user=request.user)
               return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)