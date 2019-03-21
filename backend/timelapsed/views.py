from django.shortcuts import render
from rest_framework import viewsets 

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, TopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer

class UsersView(viewsets.ModelViewSet):
  serializer_class: UsersSerializer
  model: Users

class TopicView(viewsets.ModelViewSet):
  serializer_class: TopicSerializer
  model: Topic

class EventView(viewsets.ModelViewSet):
  serializer_class: EventSerializer
  model: Event

class DateRangeView(viewsets.ModelViewSet):
  serializer_class: DateRangeSerializer
  model: Date_Range

class CardView(viewsets.ModelViewSet):
  serializer_class: CardSerializer
  model: Card
