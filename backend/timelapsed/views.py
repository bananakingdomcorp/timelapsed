from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, TopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer

class UsersView(viewsets.ModelViewSet):
  serializer_class= UsersSerializer
  queryset= Users.objects.all()
  permission_classes = (IsAuthenticated, )

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
