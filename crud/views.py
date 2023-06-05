from django.shortcuts import render
from main.models import Doacao, DoacaoSeries
from rest_framework import viewsets
from .serializer import DoacaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer

# Create your views here.


class DoacaoViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Doacao.objects.none()
    serializer_class = DoacaoSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
