from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from aquinas_automation import views
from dashing.utils import router
from aquinas_automation.widgets import *
#router = routers.DefaultRouter()
#router.register(r'sensor_readings', views.SensorReadingViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aquinas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dashboard/$', include(router.urls)),
    url(r'^lightdash/$', LightWidget.as_view(), name='Sensor Widget'),
    url(r'^tempdash/$', TemperatureWidget.as_view(), name='Sensor Widget'),
    # surl(r'^', include(router.urls)),
    url(r'^readings/$', 'aquinas_automation.views.readings', name='readings'),
    url(r'^admin/', include(admin.site.urls)),
)
