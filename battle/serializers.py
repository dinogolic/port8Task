from rest_framework import serializers
from ship.models import Ship
from ship.serializers import ShipSerializer
from .models import Battle

class BattleSerializers(serializers.ModelSerializer):
    ships = ShipSerializer(many=True, read_only=True)
    class Meta:
        model=Battle
        fields='__all__'