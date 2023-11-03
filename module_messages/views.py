from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ModuleMessageSerializer

from .models import ModuleMessages
import json
# Create your views here.


class ModuleMessagesView(APIView):
    def post(self,request):
        serializer = ModuleMessageSerializer(data=request.data.get("data"))

        if serializer.is_valid():
            new_entry = serializer.save()

            read_serializer = ModuleMessageSerializer(new_entry)

            return Response(read_serializer.data,status=201)
        return Response(serializer.errors,status=400)


        
        