from django.contrib import admin
from padam_django.apps.network.forms import BusShiftForm

from . import models


@admin.register(models.BusStop)
class BusStopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    form = BusShiftForm
