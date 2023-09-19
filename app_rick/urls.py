from .views import *
from django.urls import include,path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'character',CharacterAPIView)
router.register(r'location',LocationAPIView)
router.register(r'specie',SpecieAPIView)
router.register(r'episode',EpisodeAPIView)

urlpatterns = router.urls

'''
 urlpatterns = [
    path('character/',CharacterAPIView.as_view(),name='Character'),
    path('character/<int:CharacterId>',CharacterAPIView.as_view(),name='CharacterId'),

    
    path('specie/',SpecieAPIView.as_view(),name='Specie'),
    path('specie/<int:SpecieId>',SpecieAPIView.as_view(),name='SpecieId'),
    
    
    path('location/',LocationAPIView.as_view(),name='Location'),
    path('location/<int:LocationId>',LocationAPIView.as_view(),name='LocationId'),
    
    
    path('episode/',EpisodeAPIView.as_view(),name='Episode'),
    path('episode/<int:EpisodeId>',EpisodeAPIView.as_view(),name='EpisodeId')
]
'''