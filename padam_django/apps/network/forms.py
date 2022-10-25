from django import forms
from padam_django.apps.fleet.models import Driver, Bus
from padam_django.apps.network.models import BusStop, BusShift


class BusShiftForm(forms.ModelForm):
    class Meta:
        model = BusShift
        fields = [
            "driver",
            "bus",
            "bus_stops",
            "start_time",
            "end_time",
        ]

    def clean_start_time(self):
        data = self.cleaned_data
        raise ValueError("clean_start_time is not valid")
