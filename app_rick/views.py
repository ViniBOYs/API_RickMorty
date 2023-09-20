from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Para utilizar o JWT, não é necessário alterar a views.py

class CharacterAPIView(ModelViewSet):
    queryset = Character.objects.all() # informa p/ a lib qual as consutas a serem feitas
    serializer_class = CharacterSerializer # Informa o serializer
    filter_backends = [DjangoFilterBackend] # usa a lib django-filter
    filterset_fields = ['name', 'gender', 'species'] # Seta os campos de Filtro
    permission_classes = (IsAuthenticated,)


class SpecieAPIView(ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class LocationAPIView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type']

class EpisodeAPIView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'mainCharacter', 'episode']

   