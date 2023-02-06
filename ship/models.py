from django.db import models
from captain.models import Captain 

class Ship(models.Model):
    soldiers=models.IntegerField()
    captain = models.ForeignKey(Captain, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    x_coordinate=models.IntegerField(default=0)
    y_coordinate=models.IntegerField(default=0)
    in_battle=models.BooleanField(default=False)

    class Meta:
        db_table: 'ship'


