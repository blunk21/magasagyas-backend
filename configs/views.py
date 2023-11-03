from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Config
from .serializers import ConfigSerializer
from .forms import ConfigurationAdminForm

import json
# Create your views here.

class ConfigsView(
    APIView
):
    def get(self,request,id):
        try:
            latest_config = Config.objects.latest("id")
            if latest_config.id>id:
                return Response(latest_config.config)
            elif latest_config.id==id:
                return Response(status=200)
            else:
                return Response(status=404)
        except Config.DoesNotExist:
  
            return Response(status=404)
        
def create_new_config(request):
    if request.method == "POST":
        form = ConfigurationAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin")
    else:
        form = ConfigurationAdminForm()
    return render(request,"../templates/config_change.html", {'form': form})