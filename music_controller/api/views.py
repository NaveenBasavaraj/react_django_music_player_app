from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from api.models import Room
from api.serializers import RoomSerializer
# Create your views here.

def main(request):
    return HttpResponse('<h1>House Party</h1>')

class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# class RoomView(generics.ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
