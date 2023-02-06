from django.db import models

# Create your models here.
from django.db import models

class Captain(models.Model):
    ime = models.CharField(max_length=100)
    
    class Meta:
        db_table: 'captain'
