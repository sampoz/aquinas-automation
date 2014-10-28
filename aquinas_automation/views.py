from django.contrib.messages import api
from django.shortcuts import render
from rest_framework.response import Response
from aquinas_automation.models import SensorReading
from aquinas_automation.serializers import SensorReadingSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
# Create your views here.
class SensorReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer


@api_view(['GET', 'POST'])
def readings(request):
    """
    List all readings, or create a new snippet.
    """
    if request.method == 'GET':
        readings = SensorReading.objects.all()
        serializer = SensorReadingSerializer(readings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SensorReadingSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)