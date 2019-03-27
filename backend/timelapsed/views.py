from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, TopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer, GetUserDataSerializer

import  timelapsed.services as services

class UsersView(viewsets.ModelViewSet):
  #UsersView is designed to either authenticate or create a user.
  queryset= Users.objects.all()
  permission_classes = (IsAuthenticated, )
  serializer_class= UsersSerializer
  http_method_names = ['post']


  def create(self, request):
    queryset= Users.objects.all()
    serializer = UsersSerializer(data = request.data)
    if not serializer.is_valid():
      return Response(serializer.data, 200)

      #We created a new record
    return Response(serializer.data, 201)


class GetDataView(viewsets.ModelViewSet):
  queryset= Topic.objects.all()
  permission_classes = (IsAuthenticated, )
  serializer_class = GetUserDataSerializer
  http_method_names = ['get']

  def list(self, request):
    serializer = GetUserDataSerializer(data = request.GET)
    if serializer.is_valid():
      #send to our helper functions...
      info = services.get_user_information(serializer.data)
      print(info)
      return Response(serializer.data, 201)
      # return Response(list(info), 201)
    print(serializer.errors)
    
    return Response(serializer.data, 200)
  




class TopicView(viewsets.ModelViewSet):
  serializer_class= TopicSerializer
  queryset= Topic.objects.all()
  permission_classes = (IsAuthenticated, )

class EventView(viewsets.ModelViewSet):
  serializer_class= EventSerializer
  queryset= Event.objects.all()
  permission_classes = (IsAuthenticated, )

class DateRangeView(viewsets.ModelViewSet): 
  serializer_class= DateRangeSerializer
  queryset= Date_Range.objects.all()
  permission_classes = (IsAuthenticated, )

class CardView(viewsets.ModelViewSet):
  serializer_class= CardSerializer
  queryset= Card.objects.all()
  permission_classes = (IsAuthenticated, )
