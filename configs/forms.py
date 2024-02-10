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
    alarm1_hour = forms.IntegerField(widget=forms.NumberInput())
    alarm1_minute = forms.IntegerField(widget=forms.NumberInput())
    alarm2_hour = forms.IntegerField(widget=forms.NumberInput())
    alarm2_minute = forms.IntegerField(widget=forms.NumberInput())
    duration1 = forms.IntegerField(initial=180)
    duration2 = forms.IntegerField(initial=180)
    wakeup_frequency = forms.IntegerField(help_text="seconds",initial=3600,min_value=1200)