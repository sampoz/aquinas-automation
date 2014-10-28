from django.conf import settings
from dashing.widgets import NumberWidget
from aquinas_automation.models import SensorManager



class SensorWidget(NumberWidget):
    title = 'Sensor Data for you, kind Sir'
    def get_more_info(self):
        return 'lol'
    def get_value(self):
        return SensorManager.calculate_avg()