
from rest_framework import serializers
from tweets import models


class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tweets
        fields = '__all__'  #Todos os campos do meu model.