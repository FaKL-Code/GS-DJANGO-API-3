from rest_framework import serializers
from main.models import Doacao
from django.contrib.auth import get_user_model


class DoacaoSerializer(serializers.ModelSerializer):

    title = serializers.CharField(label="Type")
    endereco = serializers.CharField(label="Address")

    class Meta:
        model = Doacao
        fields = ['title', 'subtitle', 'endereco', 'series']
