from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tweets.api import serializers
from tweets import models


class TweetsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.TweetsSerializer
    queryset = models.Tweets.objects.all() #Todos os obj dos modelos.