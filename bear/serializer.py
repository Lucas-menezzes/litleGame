from rest_framework import serializers
from bear.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('date_created', 'date_updated', 'id')
        