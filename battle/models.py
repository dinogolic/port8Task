from django.db import models
from django.db import models

from ship.models import Ship

# Create your models here.
class Battle(models.Model):
    ships = models.ManyToManyField(Ship, related_name='battles')
    winner = models.ForeignKey(Ship, on_delete=models.SET_NULL, related_name='winning_ship', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    class Meta:
        db_table='battle'