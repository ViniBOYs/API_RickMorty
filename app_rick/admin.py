from django.contrib import admin
from .models import *

# Register your models here.

class detCharacter(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Character,detCharacter)

 
class detSpecie(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Specie,detSpecie)


class detLocation(admin.ModelAdmin):
    list_display = ('id', 'name','type','dimension')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Location,detLocation)


class detEpisode(admin.ModelAdmin):
    list_display = ('id', 'name','episode')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Episode,detEpisode)
