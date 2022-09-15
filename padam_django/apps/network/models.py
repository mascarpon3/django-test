from django.db import models
from padam_django.apps.geography.models import Place


# Create your models here.
class BusStop(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


class BusShift(models.Model):
    bus_stops = models.OneToOneField(BusStop, on_delete=models.CASCADE)
