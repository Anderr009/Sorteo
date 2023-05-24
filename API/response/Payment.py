from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest
import json

class PaymentView(APIView):
    @staticmethod
    @csrf_exempt
    def post(request):
        if request.method != 'POST':
            return Response({"mensaje": "metodo invalido"}, status=status.HTTP_204_NO_CONTENT)

        # Creando token de acceso con Sandbox
        client_id = "AcPgaSXofqtWPdc5gU3hB_YqgDGT_xICe2SYg9Hp2i-HWRM0avCqicaLFOfcP0bkGR2Kk7FMhVU8fnC1"
        client_secret = "EIw_VIadufIG4ZITgExSM_OZ2mon2G2SgjjZYyxSy5-2AWwsGNKcTW2hVaN0krfMcKU3QY8PESPoPpv8"
        
        # Creando el entorno
        environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        client = PayPalHttpClient(environment)

        data = [
            {
                "name": "Camisa",
                "description": "Camisa de manga larga",
                "quantity": 2,
                "unit_amount": {
                    "currency_code": "USD",
                    "value": "25.00"
                }
            },
            {
                "name": "Pantalón",
                "description": "Pantalón vaquero",
                "quantity": 1,
                "unit_amount": {
                    "currency_code": "USD",
                    "value": "40.00"
                }
            }
        ]

        order = OrdersCreateRequest()
        order.prefer('return=representation')
        order.request_body = {
            'intent': 'CAPTURE',
            'purchase_units': [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "90.00"
                    },
                    "items": data
                }
            ]
        }

        response = client.execute(order)
        return Response({"id": response.result.id})
