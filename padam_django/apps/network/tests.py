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
        create_stops()
        create_bus_shift()

    def test_bus_shift_has_at_least_two_stops(self):
        assert False


def create_stops():
    for place in Place.objects.all():
        BusStop(place=place, pick_up_time=_random_time()).save()


def create_bus_shift():
    bus_stops = BusStop.objects.all()
    buss = Bus.objects.all()
    drivers = Driver.objects.all()

    bus_shift = BusShift.objects.create(bus=buss[0], driver=drivers[0])
    bus_shift.bus_stops.add(bus_stops[0], bus_stops[1], bus_stops[2])
    bus_shift.save()

    bus_shift = BusShift.objects.create(bus=buss[1], driver=drivers[1])
    bus_shift.bus_stops.add(bus_stops[3], bus_stops[4], bus_stops[5])
    bus_shift.save()

    bus_shift = BusShift.objects.create(bus=buss[2], driver=drivers[2])
    bus_shift.bus_stops.add(bus_stops[6], bus_stops[7], bus_stops[8])
    bus_shift.save()

    bus_shift = BusShift.objects.create(bus=buss[3], driver=drivers[3])
    bus_shift.bus_stops.add(bus_stops[6], bus_stops[7], bus_stops[8], bus_stops[9])
    bus_shift.save()


def _random_time():
    return datetime.time(randrange(0, 24), randrange(0, 60),)
