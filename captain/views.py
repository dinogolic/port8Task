from django.shortcuts import render
from captain.models import Captain
from captain.serializers import CaptainSerializers
from rest_framework import viewsets
from rest_framework.response import Response

class CaptainViewSet(viewsets.ModelViewSet):
    queryset = Captain.objects.all()
    serializer_class = CaptainSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_data = CaptainSerializers(queryset, many=True).data        
        return Response(data=serializer_data)