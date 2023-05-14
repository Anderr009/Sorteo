from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest
#from os import getenv
import requests
import json

@api_view(['POST'])
def payment(request):
    if request.method != 'POST':
        return Response({"mensaje":"metodo invalido"},status=status.HTTP_204_NO_CONTENT)
    
    #creando token de acceso con sandbox 
    client_id = "AcPgaSXofqtWPdc5gU3hB_YqgDGT_xICe2SYg9Hp2i-HWRM0avCqicaLFOfcP0bkGR2Kk7FMhVU8fnC1"     #getenv("CLIENT_ID")
    client_secret ="EIw_VIadufIG4ZITgExSM_OZ2mon2G2SgjjZYyxSy5-2AWwsGNKcTW2hVaN0krfMcKU3QY8PESPoPpv8"     #getenv("CLIENT_SECRET")
    #creando el entorno
    environment = SandboxEnvironment(client_id=client_id,client_secret=client_secret)
    client = PayPalHttpClient(environment)
    data = json.loads(request.body)
    order = OrdersCreateRequest()
    order.prefer('return=representation')
    order.request_body
    (
        {
            'intent':'CAPTURE',
            'purchase_units': [
                {
                    "amount":{
                        "currency_code":"USD",
                        "value":"26.00"
                    }
                } 
            ],
            "items":data
        }
    )
    response = client.execute(order)
    return Response({"id":response.result.id})