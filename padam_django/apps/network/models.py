from django.db import models
from padam_django.apps.geography.models import Place
from padam_django.apps.fleet.models import Bus, Driver


class BusStop(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    pick_up_time = models.TimeField(null=False)


class BusShift(models.Model):
    driver = models.ForeignKey(Driver, null=False, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, null=False, on_delete=models.CASCADE)
    bus_stops = models.ManyToManyField(BusStop)

    def save(self, *args, **kwargs):
        if self.bus_stops.count() < 2:
            raise ValueError("a bus_shift must have at least two stops")
        super(BusShift, self).save(*args, **kwargs)
