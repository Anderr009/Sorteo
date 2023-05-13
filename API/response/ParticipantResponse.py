from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from API.serializers.SerializerPart import Participante_Serializer
from API.models import Participante
from random import randint
import requests
import json

@api_view(['POST'])
def Participant_Register(request):
    if request.method == 'POST':
        data = request.body
        dataDict = json.loads(data)
        #construyendo el obj participante
        try:
            resp = requests.get(f"https://api.digital.gob.do/v3/cedulas/{dataDict['cedula']}/validate")
            valid = json.loads(resp.text)
            if not valid['valid']: 
                return Response({'mensaje':'cedula no valida'},status= status.HTTP_400_BAD_REQUEST)
            prt = Participante(**dataDict)
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

