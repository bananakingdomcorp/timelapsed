from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card

from .serializers import UsersSerializer, TopicSerializer, EventSerializer, DateRangeSerializer, CardSerializer

class UsersView(viewsets.ModelViewSet):
  #UsersView is designed to either authenticate or create a user.
  authentication_classes = (TokenAuthentication,)
  queryset= Users.objects.all()
  permission_classes = (IsAuthenticated, )
  serializer_class= UsersSerializer


  @api_view(['POST'])
  def check_for_user(self, request):
    serializer = UsersSerializer
    # print(request.data)
    return Response(serializer.data)




class TopicView(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)
  serializer_class= TopicSerializer
  queryset= Topic.objects.all()
  permission_classes = (IsAuthenticated, )

class EventView(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)
  serializer_class= EventSerializer
  queryset= Event.objects.all()
  permission_classes = (IsAuthenticated, )

class DateRangeView(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)  
  serializer_class= DateRangeSerializer
  queryset= Date_Range.objects.all()
  permission_classes = (IsAuthenticated, )

class CardView(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)
  serializer_class= CardSerializer
  queryset= Card.objects.all()
  permission_classes = (IsAuthenticated, )
