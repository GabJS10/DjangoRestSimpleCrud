from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Characters
from .serializers import CharactersSerializer
# Create your views here.

class CharactersList(generics.ListCreateAPIView):
     queryset = Characters.objects.all()
     serializer_class = CharactersSerializer

class CharactersDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Characters.objects.all()
     serializer_class = CharactersSerializer
