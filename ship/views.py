import random
from rest_framework.response import Response
import string
from rest_framework import viewsets, status
from rest_framework.decorators import action

from captain.models import Captain
from ship.models import Ship
from ship.serializers import ShipSerializer

class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()

    def list(self, request, *args, **kwargs):
        # Ovo je kad dodje get request iz postavke.
        niz_vojnika = request.query_params.get('ships').split(',')
        kapetani = []
        for i in range(len(niz_vojnika)):
            kapetani.append(Captain(ime=''.join(random.choices(string.ascii_letters, k=5))))

        Captain.objects.bulk_create(kapetani)

        niz_brodova = []
        for vojnici in niz_vojnika:
            niz_brodova.append(Ship(soldiers=vojnici, name=''.join(random.choices(string.ascii_letters, k=5)), x_coordinate=random.randint(-100,100), y_coordinate=random.randint(-100,100)))
        Ship.objects.bulk_create(niz_brodova)
        
        for i in range(len(niz_brodova)):
            niz_brodova[i].captain = kapetani[i]
            niz_brodova[i].save()

        return Response({'dobar' : 'dobar pravo'})

    @action(detail=True, methods=['PATCH'])
    def update_koordinate(self, request, *args, **kwargs):
        ship = self.get_object()
        serializer = ShipSerializer(ship, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
