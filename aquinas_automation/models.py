from django.db import models
from django.db.models import Avg
# Create your models here.

class SensorReading(models.Model):
    sensor_name = models.CharField(max_length=100)
    value = models.IntegerField()
    created = models.DateTimeField('date recorded', auto_now_add=True, blank=True)

class SensorManager(models.Manager):
    @staticmethod
    def calculate_avg():
        readings = SensorReading.objects.all()
        s = 0
        for reading in readings:
            s += reading.value
        return s/len(readings)
