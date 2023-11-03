from rest_framework import serializers

from .models import ModuleMessages

import datetime


class ModuleMessageSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        ts = self.initial_data.get("ts")
        timestamp = datetime.datetime.fromtimestamp(ts)
        readable_time = f"{timestamp.year}-{timestamp.month}-{timestamp.day} {timestamp.hour}:{timestamp.minute}:{timestamp.second}"
        return ModuleMessages.objects.create(data=validated_data,timestamp=timestamp)
    
    class Meta:
        model=ModuleMessages
        managed = False
        fields=("id","server_timestamp")
