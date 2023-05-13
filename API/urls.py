from django.urls import path
from API.response.ParticipantResponse import Participant_Register
from API.response.Payment import payment
urlpatterns = [
    path('prueba/', Participant_Register),
    path('paypal/', payment)
]
