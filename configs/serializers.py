from rest_framework import serializers
from .models import Config

class ConfigSerializer(serializers.ModelSerializer):
    config_text = serializers.JSONField()

    def create(self, validated_data):

        return Config.objects.create(text=validated_data.get("text"))
    

class Meta:
    model = Config
    fields = (
        "id",
        "config"
    )