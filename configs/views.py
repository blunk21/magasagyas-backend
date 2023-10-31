from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Config
from .serializers import ConfigSerializer

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
            else:
                return Response(status=404)
        except Config.DoesNotExist:
  
            return Response(status=404)
        
        