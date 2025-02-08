from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition

from drones.serializers import DroneCategorySerializer
from drones.serializers import DroneSerializer
from drones.serializers import CompetitionSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer


# Create your views here.
class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'drone-category-list'

class DroneCategoryDetail(generics.RetreiveUpdateDeleteAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'drone-category-detail'

class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'

class PilotDetail(generics.RetreiveUpdateDeleteAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition-list'

class CompetitionDetails(generics.RetreiveUpdateDeleteAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-details'