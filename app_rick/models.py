from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.


class Specie(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=150, null=False)
    gender = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(default=timezone.now())
    species = models.ForeignKey(Specie, related_name="species", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=150, null=False)
    dimension = models.CharField(max_length=150, null=False)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
    
class Episode(models.Model):
    name = models.CharField(max_length=150, null=False)
    episode = models.CharField(max_length=150, null=False)
    air_date = models.DateTimeField(default=timezone.now())
    mainCharacter = models.ForeignKey(Character, related_name="character", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name









