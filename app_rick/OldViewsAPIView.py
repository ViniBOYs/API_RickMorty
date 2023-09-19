'''




Views.py com a biblioteca antiga, APIview




'''









from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.


class CharacterAPIView(APIView):
    def get(self, request, CharacterId = ''):
        #se o get não tiver o filtro de id:
        if CharacterId == '':   
            CharacterFound = ''
            #se passarem o filtro de 'name'
            if 'name' in request.GET and 'gender' in request.GET:
                nameToFilter = request.GET['name']
                eyeToFilter = request.GET['gender']
                CharacterFound = Character.objects.filter(name__contains=nameToFilter).filter(gender__contains=eyeToFilter)                
            elif 'name' in request.GET:
                #pegando o parâmetro que foi informado!
                nameToFilter = request.GET['name']
                #SELECT *FROM Character WHERE NAME LIKE %nameToFilter%;
                CharacterFound = Character.objects.filter(name__contains=nameToFilter)
            elif 'gender' in request.GET:
                eyeToFilter = request.GET['gender']
                CharacterFound = Character.objects.filter(gender__contains=eyeToFilter)    
            else:
                #seleciona tudo!     
                CharacterFound = Character.objects.all() #select *from Character; #PYTHON
            serializer = CharacterSerializer(CharacterFound, many=True) #JSON
            return Response(status=200, data=serializer.data) #devolvendo ao cliente o JSON!
        #busca por Character id:
        try:
            CharacterFound = Character.objects.get(id=CharacterId) #select *from Character where id = CharacterId 
            serializer = CharacterSerializer(CharacterFound, many=False) #JSON
            return Response(status=200,data=serializer.data)
        except Character.DoesNotExist:
            return Response(status=404,  data="Character not Found!!!!")
    
    def post(self, request):
        # Pega o Json do cliente e guarda na variavel
        characterJson = request.data
        # Converte Json em Python!!!
        characterSerialized = CharacterSerializer(data=characterJson, many=False)
        # Verificar se os dados estão coerentes!
        if characterSerialized.is_valid():
            # Salvando no banco de dados
            characterSerialized.save()
            return Response(status=201, data=characterSerialized.data)
        return Response(status=400, data="Manda certo cabeça de bagre!")
    
    def delete(self, request, CharacterId = ''):
        if (CharacterId != ''):
            # Procurar a pessoa com o Id!
            characterFound = Character.objects.get(id=CharacterId)
            # Deletando o Usuario
            characterFound.delete()
            return Response(status=200, data='People successfully deleted')
        # Cliente da API não passou o CharacterId para deletar!
        return Response(status=400, data="CharacterId must be given!")
    
    def put(self, request, CharacterId):
        if (CharacterId != ''):
            # Procurar o Antigo no banco
            characterFound = Character.objects.get(id=CharacterId)
            # Coletar o novo que veio JSON:
            characterToUpdateJSON = request.data
            # Faz o serializer substituir o novo pelo antigo e converter para python
            serializedCharacter = CharacterSerializer(characterFound, data=characterToUpdateJSON)
            # Verifica se a conversão é válida
            if(serializedCharacter.is_valid()):
                # Salva no banco de dados
                serializedCharacter.save()
                return Response(status=200, data=serializedCharacter.data)
            Response(status=400, data="Invalid Data!")
        return Response(status=400, data="CharacterId must be given!")
    


class SpecieAPIView(APIView):
    def get(self,request, SpecieId = ''):
        if SpecieId == '':
            SpecieFound = Specie.objects.all()
            serializer = SpecieSerializer(SpecieFound, many=True)
            return Response(serializer.data)
        try:
            SpecieFound = Specie.objects.get(id=SpecieId)
            serializer = SpecieSerializer(SpecieFound, many=False)
            return Response(serializer.data)
        except Specie.DoesNotExist:
            return Response(status=404, data="Specie not Found!!!")

    def post(self, request, SpecieId = ''):
        specieJson = request.data
        specieSerialized = SpecieSerializer(data=specieJson, many=False)
        if specieSerialized.is_valid():
            specieSerialized.save()
            return Response(status=201, data=specieSerialized.data)
        return Response(status=404, data="Os dados enviados estão incorretos, Jamanta!")

    def delete(self, request, SpecieId = ''):
        if (SpecieId != ''):
            specieFound = Specie.objects.get(id=SpecieId)
            specieFound.delete()
            return Response(status=200, data="Specie successfully deleted")
        return Response(status=404, data="Specie Id must be given!")

    def put(self, request, SpecieId = ''):
        if (SpecieId != ''):
            specieFound = Specie.objects.get(id=SpecieId)
            specieToUpdateJSON = request.data
            serializedSpecie = SpecieSerializer(specieFound, data=specieToUpdateJSON)
            if(serializedSpecie.is_valid()):
                serializedSpecie.save()
                return Response(status=200, data=serializedSpecie.data)
            Response(status=400, data="Invalid Data!")
        return Response(status=400, data="SpecieId must be given!")
    
class LocationAPIView(APIView):
    def get(self,request, LocationId = ''):
        if LocationId == '': 
            LocationFound = Location.objects.all()
            serializer = LocationSerializer(LocationFound, many=True)
            return Response(serializer.data)
        try:
            LocationFound = Location.objects.get(id=LocationId)
            serializer = LocationSerializer(LocationFound, many=False)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response(status=404, data="People not Found!!!")  
            
    def post(self, request):
        LocationJson = request.data
        LocationSerialized = LocationSerializer(data=LocationJson, many=False)
        if LocationSerialized.is_valid():
            LocationSerialized.save()
            return Response(status=201, data=LocationSerialized.data)
        return Response(status=400, data="Manda certo cabeça de bagre!")
    
    def delete(self, request, LocationId = ''):
        if (LocationId != ''):
            LocationFound = Location.objects.get(id=LocationId)
            LocationFound.delete()
            return Response(status=200, data='Location successfully deleted')
        return Response(status=400, data="LocationId must be given!")
    
    def put(self, request, LocationId):
        if (LocationId != ''):
            LocationFound = Location.objects.get(id=LocationId)
            LocationToUpdateJSON = request.data
            serializedLocation = LocationSerializer(LocationFound, data=LocationToUpdateJSON)
            if(serializedLocation.is_valid()):
                serializedLocation.save()
                return Response(status=200, data=serializedLocation.data)
            Response(status=400, data="Invalid Data!")
        return Response(status=400, data="LocationId must be given!")
    
class EpisodeAPIView(APIView):
    def get(self,request, EpisodeId = ''):
        if EpisodeId == '': 
            EpisodeFound = Episode.objects.all()
            serializer = EpisodeSerializer(EpisodeFound, many=True)
            return Response(serializer.data)
        try:
            EpisodeFound = Episode.objects.get(id=EpisodeId)
            serializer = EpisodeSerializer(EpisodeFound, many=False)
            return Response(serializer.data)
        except Episode.DoesNotExist:
            return Response(status=404, data="People not Found!!!")  
            
    def post(self, request):
        EpisodeJson = request.data
        EpisodeSerialized = EpisodeSerializer(data=EpisodeJson, many=False)
        if EpisodeSerialized.is_valid():
            EpisodeSerialized.save()
            return Response(status=201, data=EpisodeSerialized.data)
        return Response(status=400, data="Manda certo cabeça de bagre!")
    
    def delete(self, request, EpisodeId = ''):
        if (EpisodeId != ''):
            EpisodeFound = Episode.objects.get(id=EpisodeId)
            EpisodeFound.delete()
            return Response(status=200, data='Episode successfully deleted')
        return Response(status=400, data="EpisodeId must be given!")
    
    def put(self, request, EpisodeId):
        if (EpisodeId != ''):
            EpisodeFound = Episode.objects.get(id=EpisodeId)
            EpisodeToUpdateJSON = request.data
            serializedEpisode = EpisodeSerializer(EpisodeFound, data=EpisodeToUpdateJSON)
            if(serializedEpisode.is_valid()):
                serializedEpisode.save()
                return Response(status=200, data=serializedEpisode.data)
            Response(status=400, data="Invalid Data!")
        return Response(status=400, data="EpisodeId must be given!")