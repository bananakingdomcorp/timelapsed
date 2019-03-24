from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, TopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer

class UsersView(viewsets.ModelViewSet):
  #UsersView is designed to either authenticate or create a user.
  queryset= Users.objects.all()
  permission_classes = (IsAuthenticated, )
  serializer_class= UsersSerializer
  @api_view(['POST'])
  def check_for_user(request):

    print(request.data)




    return 'hello'




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
