import requests

headers = {
    'Content-Type': 'application/json',
    'PayPal-Request-Id': '7b92603e-77ed-4896-8e78-5dea2050476a',
    'Authorization': 'Bearer A21AAIgwgLWvweDjHEoAKF5brHaRu4eG3-xrqQZDCBvyBeLIUxrE2MS-SyoSM4oRMc4rM7MdkhN7j5IIMY4k1IbGd2ggDkowg',
}

data = '''
{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      },
      "shipping": {
        "address": {
          "address_line_1": "123 Street",
          "admin_area_2": "City",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    }
  ],
  "payment_source": {
    "paypal": {
      "experience_context": {
        "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
        "payment_method_selected": "PAYPAL",
        "brand_name": "EXAMPLE INC",
        "locale": "en-US",
        "landing_page": "LOGIN",
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "user_action": "PAY_NOW",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
'''

response = requests.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, data=data)

# Verificar el estado de la respuesta
if response.status_code == 201:
    # Solicitud exitosa
    order_id = response.json().get('id')
    print(f"ID de la orden: {order_id}")
    
    # Obtener el enlace para la acción del pagador
    payer_action_url = None
    links = response.json().get('links')
    for link in links:
        if link.get('rel') == 'payer-action':
            payer_action_url = link.get('href')
            break
    
    if payer_action_url:
        print(f"Acción requerida por el pagador: {payer_action_url}")
    else:
        print("No se encontró enlace para la acción del pagador")
else:
    # Error en la solicitud
    print(f"Error en la solicitud: {response.text}")
