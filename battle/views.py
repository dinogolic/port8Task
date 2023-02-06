from django.shortcuts import render

# Create your views here.
from battle.models import Battle
from .serializers import BattleSerializers
from rest_framework import viewsets
from ship.models import Ship
from ship.serializers import ShipSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
import math
import random

def provjeri_odstojanje(ship1, ship2):
        return math.sqrt((ship2.x_coordinate - ship1.x_coordinate)**2 + (ship2.y_coordinate - ship1.y_coordinate)**2) < 150


class BattleViewset(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializers

    def create(self, request, *args, **kwargs):
        ship_ids = request.data.get('ships')
        ships = Ship.objects.filter(id__in=ship_ids)
        battle = Battle.objects.create()
        battle.ships.set(ships)
        battle.is_active=True
        battle.save()
        Ship.objects.filter(id__in=ship_ids).update(in_battle=True)
        serializer = self.get_serializer(battle)
        return Response(serializer.data)




    @action(detail=True, methods=['PATCH'])
    def simuliraj_napad(self, request, *args, **kwargs):
        napada_id = request.data.get('napada')
        koga_napada = request.data.get('koga_napada')
        try:
            bitka = self.get_object()
            idbrodova = list(bitka.ships.all().values_list('id', flat=True))
            ship1 = Ship.objects.filter(id=napada_id, in_battle=True, id__in=idbrodova).get()
            ship2 = Ship.objects.filter(id=koga_napada, in_battle=True, id__in=idbrodova).get()
            if provjeri_odstojanje(ship1,ship2):
                ship2.soldiers = ship2.soldiers-random.randint(1,5)
                if ship2.soldiers == 0:
                    ship2.delete()
                ship2.save()
                return Response("Napad uspjesno proso")
            else:
                return Response("Brodovi su previse udaljeni.")

        except ObjectDoesNotExist:
            return Response("NE VALJA ID")


    @action(detail=True, methods=['PATCH'])
    def zavrsi_bitku(self, request, *args, **kwargs):
            bitka = self.get_object()
            idbrodova = list(bitka.ships.all().values_list('id', flat=True))
            brodovi = Ship.objects.filter(id__in=idbrodova)
            pobjednik = max(brodovi, key=lambda x: x.soldiers)
            bitka.is_active = False
            bitka.winner = pobjednik
            bitka.save()
            serializer=ShipSerializer(pobjednik) 
            #pobjednik je brod koji ima najviše vojnika nakon završetka borbe. 
            return Response(serializer.data)