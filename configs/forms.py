from django.forms import ModelForm

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

class ConfigurationAdminForm(ModelForm):
    """Form class for model dynamicconfig.DynamicConfiguration."""

    def __init__(self, *args, **kwargs):
        """Override init method to set initial value for config_data field."""
        super().__init__(*args, **kwargs)
        if not self.initial:
            self.initial = {}
        if "config_data" not in self.initial:
            self.initial["config_data"] = get_initial_config_data_value

    class Meta:
        """Meta class for DynamicConfigurationAdminForm."""

        model = Config
        fields = (
            "config",
        )