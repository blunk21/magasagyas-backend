from rest_framework import serializers

from .models import ModuleMessages

import datetime


class ModuleMessageSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        ts= self.initial_data.get("ts")
        if ts is None:
            raise serializers.ValidationError({"error": "Module message is missing timestamp"})
        timestamp = datetime.datetime.fromtimestamp(ts)
        readable_time = f"{timestamp.year}-{timestamp.month}-{timestamp.day} {timestamp.hour}:{timestamp.minute}:{timestamp.second}"

        validated_data = self.initial_data
        return ModuleMessages.objects.create(data=validated_data,timestamp=readable_time)
    
    class Meta:
        model=ModuleMessages
        managed = False
        fields=("id","server_timestamp")
