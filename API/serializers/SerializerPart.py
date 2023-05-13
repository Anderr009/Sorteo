from rest_framework import serializers
from API.models import Participante
#serializador para registrar
class Participante_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'