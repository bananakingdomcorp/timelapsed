from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, AddTopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer

import  timelapsed.services as services

class UsersView(viewsets.ModelViewSet):
  #UsersView is designed to either create a user, or respond back with a users data.
  queryset= Users.objects.all()
  permission_classes = (IsAuthenticated, )
  serializer_class= UsersSerializer
  http_method_names = ['post']


  def create(self, request):
    queryset= Users.objects.all()
    serializer = UsersSerializer(data = request.data)
    if not serializer.is_valid():
      info = services.get_user_information(serializer.data)
      #Returning information about an exising record.
      return Response(info, 200)

      #We created a new record
    return Response(serializer.data, 201)




class AddTopicView(viewsets.ModelViewSet):
  serializer_class= AddTopicSerializer
  queryset= Topic.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['post']

  def create (self, request):
    serializer = AddTopicSerializer(data = request.data)
    if serializer.is_valid():
      serializer.create(serializer.data, request.user.email)
      

    print(serializer.data, 'SERIALIZED')











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
