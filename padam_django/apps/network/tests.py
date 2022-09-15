from django.test import TestCase
from padam_django.apps.network.models import BusStop, BusShift

from padam_django.apps.geography.models import Place
from django.core import management


class NetworkTestCse(TestCase):
    def setUp(self):
        management.call_command('create_users', number=5)
        management.call_command('create_drivers', number=5)
        management.call_command('create_buses', number=10)
        management.call_command('create_places', number=30)

    def test_add_bus_shift(self):
        place = Place.objects.first()
        bus_stop = BusStop(place=place)
        bus_stop.save()
        assert False
