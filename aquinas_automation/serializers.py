from rest_framework import serializers
from aquinas_automation.models import SensorReading


class SensorReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorReading
        fields = ('created', 'sensor_name', 'value')
