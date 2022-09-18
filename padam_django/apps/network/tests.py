import datetime
from random import randrange, seed

from django.test import TestCase
from django.core import management

from padam_django.apps.geography.models import Place
from padam_django.apps.network.models import BusStop, BusShift
from padam_django.apps.fleet.models import Bus, Driver


class NetworkTestCse(TestCase):
    def setUp(self):
        seed(1)
        management.call_command('create_users', number=5)
        management.call_command('create_drivers', number=5)
        management.call_command('create_buses', number=10)
        management.call_command('create_places', number=30)
        self.places = Place.objects.all()
        self.buss = Bus.objects.all()
        self.drivers = Driver.objects.all()

        self.create_bus_stops()
        self.bus_stops = BusStop.objects.all()

        self.create_bus_shifts()
        self.bus_shifts = BusShift.objects.all()

    @staticmethod
    def test_cant_add_same_bus_on_two_shifts():
        bus_stops = BusStop.objects.all()
        buss = Bus.objects.all()
        drivers = Driver.objects.all()
        bus_shifts = BusShift.objects.all()

        bus_shift = BusShift.objects.create(
            bus=buss[0],
            driver=drivers[0],
            bus_stops=(bus_stops[0], bus_stops[1])
        )
        assert True

    def test_start_and_end_time_computation(self):
        bus_shift = BusShift.objects.create(
            bus=self.buss[2],
            driver=self.drivers[2],
            bus_stops=(self.bus_stops[0], self.bus_stops[1], self.bus_stops[2])
        )

        assert bus_shift.start_time == min(
            self.bus_stops[0].pick_up_time,
            self.bus_stops[1].pick_up_time,
            self.bus_stops[2].pick_up_time
        )
        assert bus_shift.end_time == max(
            self.bus_stops[0].pick_up_time,
            self.bus_stops[1].pick_up_time,
            self.bus_stops[2].pick_up_time
        )

    def create_bus_stops(self):
        for place in self.places:
            BusStop(place=place, pick_up_time=_get_random_time()).save()

    def create_bus_shifts(self):
        BusShift.objects.create(
            bus=self.buss[0],
            driver=self.drivers[0],
            bus_stops=(self.bus_stops[0], self.bus_stops[1], self.bus_stops[2]),
        )
        BusShift.objects.create(
            bus=self.buss[1],
            driver=self.drivers[1],
            bus_stops=(self.bus_stops[4], self.bus_stops[5], self.bus_stops[6])
        )


def _get_random_time():
    return datetime.time(randrange(0, 24), randrange(0, 60),)
