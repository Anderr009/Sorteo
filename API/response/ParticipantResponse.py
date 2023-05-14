from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from API.serializers.SerializerPart import Participante_Serializer
from API.models import Participante
from random import randint
import requests
import json

@api_view(['POST','GET'])
def Participant_Register(request):
    if request.method == 'GET':
        part = Participante.objects.all()
        serializer = Participante_Serializer(part,many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    #en caso de ser POST
    if request.method == 'POST':
        data = request.body
        dataDict = json.loads(data)
        #construyendo el obj participante
        try:
            resp = requests.get(f"https://api.digital.gob.do/v3/cedulas/{dataDict['cedula']}/validate")
            valid = json.loads(resp.text)
            if not valid['valid']: 
                return Response({'mensaje':'cedula no valida'},status= status.HTTP_400_BAD_REQUEST)
            
            while True:
                cod = GetCode()
                try:
                    #Buscando un codigo unico 
                    tempPrt = Participante.objects.get(codigo=cod)
                except ObjectDoesNotExist:
                    break;
            prt = Participante(**dataDict)
            prt.codigo = cod
            prt.save()
            return Response({"mensaje":"creado"},status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"mensaje":"Parametros equivocados"},status=status.HTTP_406_NOT_ACCEPTABLE)


#obtener codigo de mierda de 8 digitos de l diablo
def GetCode():
    cod = ""
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(8):
        letter = randint(0,len(letras)- 1)
        cod = cod + letras[letter]
    return cod

