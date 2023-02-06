from rest_framework import serializers
from captain.models import Captain


class CaptainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Captain
        fields = '__all__'
