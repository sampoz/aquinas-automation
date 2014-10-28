from django.conf import settings
from dashing.widgets import NumberWidget
from aquinas_automation.models import SensorManager



class LightWidget(NumberWidget):
    title = 'Amount of Light'
    def get_more_info(self):
        return 'In sensors terms'
    def get_value(self):
        return SensorManager.calculate_avg()


class TemperatureWidget(NumberWidget):
    title = 'Temperature'
    def get_more_info(self):
        return 'In Celcius'
    def get_value(self):
        return "24.00"