from django.db import models
from django.db.models.query import QuerySet


class BusShiftManager(models.Manager):

    def get_query_set(self):
        return QuerySet(self.model, self._db)

    def create(self, *args, **kwargs):
        nb_bus_stops = len(kwargs["bus_stops"])
        if nb_bus_stops < 2:
            raise ValueError(f"a bus shift must have at least two bus stops, got {nb_bus_stops}")
        bus_shift = self.create_bus_shift(**kwargs)
        return bus_shift

    def create_bus_shift(self, bus, driver, bus_stops):
        bus_shift = self.get_query_set().create(bus=bus, driver=driver)
        bus_shift.save()
        bus_shift.bus_stops.add(*bus_stops)
        bus_shift.save()
        return bus_shift
