from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Config
from .serializers import ConfigSerializer
from .forms import ConfigCreationForm

import json

# Create your views here.


class ConfigsView(APIView):
    def get(self, request, id):
        try:
            latest_config = Config.objects.latest("id")
            if latest_config.id > id:
                latest_config.config["id"] = latest_config.id 
                return Response(latest_config.config)
            elif latest_config.id == id:
                return Response(status=200)
            else:
                return Response(status=404)
        except Config.DoesNotExist:
            return Response(status=404)


def create_new_config(request):
    if request.method == "POST":
        form = ConfigCreationForm(request.POST)
        if form.is_valid():
            config_data = {
                "alrm1": [form.cleaned_data["alarm1_hour"], form.cleaned_data["alarm1_minute"]],
                "alrm2": [form.cleaned_data["alarm2_hour"],form.cleaned_data["alarm2_minute"]],
                "dur1": form.cleaned_data["duration1"],
                "dur2": form.cleaned_data["duration2"],
                "mes_freq": form.cleaned_data["wakeup_frequency"],
            }
            Config.objects.create(config=config_data)
            return redirect("create_new_config")
    else:
        form = ConfigCreationForm()
    return render(request, "config_change.html", {"form": form})
