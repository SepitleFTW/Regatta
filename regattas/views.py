from django.shortcuts import render
from django.http import HttpResponse
from .models import Regatta, Race, Result, Club
from rest_framework import viewsets
from .serializers import RegattaSerializer, RaceSerializer, ResultSerializer, ClubSerializer

def index(request):
    return HttpResponse("Hello and welcome to beginning of regatta results!")

# handling api logic for CRUD with ViewSets
class RegattaViewSet(viewsets.ModelViewSet):
    queryset = Regatta.objects.all()
    serializer_class = RegattaSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer