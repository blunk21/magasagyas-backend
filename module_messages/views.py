from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ModuleMessageSerializer

from .models import ModuleMessages
import json
# Create your views here.


from rest_framework import status

class ModuleMessagesView(APIView):
    def post(self, request):
        data = request.data.get("data")  # Assuming 'data' is a list of JSON objects
        if not isinstance(data, list):
            return Response({"error": "Expected a list of data"}, status=status.HTTP_400_BAD_REQUEST)

        responses = []
        for item in data:
            serializer = ModuleMessageSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                responses.append({"status": "success", "data": serializer.data})
            else:
                responses.append({"status": "error", "errors": serializer.errors})

        return Response(responses, status=status.HTTP_200_OK)



        
        