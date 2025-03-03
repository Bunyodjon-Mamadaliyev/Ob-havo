from rest_framework import serializers
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'temperature', 'humidity',
                  'pressure', 'wind_speed', 'wind_direction',
                  'precipitation', 'recorded_at']
