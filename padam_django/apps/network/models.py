from django.db import models
from padam_django.apps.geography.models import Place
from padam_django.apps.users.models import User
from padam_django.apps.fleet.models import Bus


class BusStop(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        BusStop.objects.all()
        super(BusStop, self).save(*args, **kwargs)


class BusShift(models.Model):
    start_datatime = models.DateTimeField(null=False)
    end_datatime = models.DateTimeField(null=False)
    driver = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, null=False, on_delete=models.CASCADE)


class BusShiftToBusStops(models.Model):
    bus_shift = models.ForeignKey(BusShift, on_delete=models.CASCADE)
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    position = models.IntegerField(null=False)
