from django.forms import ModelForm,Form
from django import forms
from datetime import datetime

from .models import Config


def get_initial_config_data_value():
    """Function that returns a default initial value.

    Used for field config_data of :dynamicconfig.models:DynamicConfiguration.
    """
    return {
        "sysconfig":{
            "measurement_freq_sec": 1200,
            "irrigation_duration_sec":120,
            "irrigation_times":["08:00,18:00"]
        }
    }

class ConfigCreationForm(Form):
    alarm1 = forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    alarm2 = forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    duration1 = forms.IntegerField(help_text="Duration of irrigation in seconds for alarm1",initial=180,min_value=60)
    duration2 = forms.IntegerField(help_text="Duration of irrigation in seconds for alarm2",initial=180,min_value=60)
    data_send_frequency = forms.IntegerField(help_text="Wakeup frequency of the module in seconds",initial=3600,min_value=1200)