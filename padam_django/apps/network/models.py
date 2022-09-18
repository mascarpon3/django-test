from django.db import models
from padam_django.apps.geography.models import Place
from padam_django.apps.fleet.models import Bus, Driver
from django.db.models import Max, Min


class BusStop(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    pick_up_time = models.TimeField(null=False)


class BusShift(models.Model):
    driver = models.ForeignKey(Driver, null=False, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, null=False, on_delete=models.CASCADE)
    bus_stops = models.ManyToManyField(BusStop)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            if self.bus_stops:
                self.update_start_and_end_time()

        super(BusShift, self).save(*args, **kwargs)

    def update_start_and_end_time(self):
        self.start_time = self.bus_stops.values("pick_up_time").aggregate(Min('pick_up_time'))['pick_up_time__min']
        self.end_time = self.bus_stops.values("pick_up_time").aggregate(Max('pick_up_time'))['pick_up_time__max']
