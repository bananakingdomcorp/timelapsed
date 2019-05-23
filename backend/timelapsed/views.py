from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

from .models import Users, Topic, Event, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships

from .serializers import UsersSerializer, AddTopicSerializer, CreateCardSerializer, EditTopicSerializer , DeleteTopicSerializer, DeleteCardSerializer, UpdateCardSerializer, CreateSubclassSerializer, TopicRelationshipsSerializer, CardRelationshipsSerializer, EditSubclassSerializer, DeleteSubclassSerializer, GetSubclassSerializer, CreateSubclassRelationshipSerializer 

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




class TopicView(viewsets.ModelViewSet):
  serializer_class= AddTopicSerializer
  queryset= Topic.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['post', 'update', 'put', 'delete']

  def create (self, request):
    serializer = AddTopicSerializer(data = request.data)
    if serializer.is_valid():
      created = serializer.create(serializer.data, request.user.email)

    return Response(created, 201)

  def update(self, request, pk):
    '''
    How does the update work:

    There may be multiple positional arguments. 

    If there are, then a switch is happening. 

    If there are not, then we are just updating a title.

    '''
    serializer = EditTopicSerializer(data = request.data)
    if serializer.is_valid():
      serializer.update(serializer.data, pk)
      return Response('updated', 200)
    print(serializer.errors)

    return Response('NONE VALID', 200) #consider adding a default failure status code. 

    

  def destroy(self, request, pk):
    serializer = DeleteTopicSerializer(data = {id:pk})
    if serializer.is_valid():
      serializer.delete(pk)
      return Response('deleted', 204)
    return Response('Delete Failed', 200) #consider changing status code



class CardView(viewsets.ModelViewSet):
  serializer_class= CreateCardSerializer
  queryset= Card.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['post', 'put', 'delete' ]

  def create(self, request):
    serializer = CreateCardSerializer(data= request.data)
    if(serializer.is_valid()):
      created =  serializer.create(serializer.data, request.user.email)
      return Response(created , 201)
    else:
      print(serializer.errors)

    return Response('INVALID', 200)

  def update(self, request, pk):
    print(request.data, 'REQUEST')
    serializer = UpdateCardSerializer(data = request.data)
    if(serializer.is_valid()):
      updated = serializer.update(serializer.data, pk, request.user.email)
      return Response(updated, 200)
    print(serializer.errors)
    return Response('failed',400)

  def destroy(self, request, pk):
    serializer = DeleteCardSerializer(data = {id:pk})
    if(serializer.is_valid()):
      created = serializer.destroy(pk)
      return Response('Deleted', 204)

    return Response('Failed', 200)

    return 

class SubclassesView(views.ModelViewSet):
  serializer_class= CreateSubclassSerializer
  queryset= Subclass.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['get', 'post', 'put', 'delete' ]

  def get(self, request):
    serializer = GetSubclassSerializer(data = request.data)
    if serializer.is_valid():
      found = serializer.get(serializer.data)
    return Response(found, 200)

    print(serializer.errors)
    return Response('Error finding Subclass', 400)


  def create(self, request):
    serializer = CreateSubclassSerializer(data = request.data)
    if serializer.is_valid():
      created = serializer.create(serializer.data, request.user.email)
    return Response(created, 201)
    
    print(serializer.errors)
    return Response('Creation Failed', 400)


  def update(self, request, pk):
    serializer = EditSubclassSerializer(data = request.data)
    if serializer.is_valid():
      serializer.update(serializer.data, pk, request.user.email)
    return Response('Updated', 200)

    print(serializer.errors)
    return ('Update Failed', 400)


  def destroy(self, request, pk):
    #request has the id of the card
    serializer = DeleteSubclassSerializer(data = request.data)
    if serializer.is_valid():
      serializer.destroy(pk)
    return Response('Deleted', 204)

    print(serializer.errors)

    return Response('Delete failed', 400)



# class SubclassRelationshipsView(views.ModelViewSet):








class TopicRelationshipsView(views.ModelViewSet):
  serializer_class= TopicRelationshipsSerializer
  queryset= Topic_Relationships.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['post', 'put', 'delete' ]

  def create(self, request):
    
    return
  def update(self, request):
    return
  def destroy(self, request):
    return

class CardRelationshipsView(views.ModelViewSet):
  serializer_class= CardRelationshipsSerializer
  queryset= Card_Relationships.objects.all()
  permission_classes = (IsAuthenticated, )
  http_method_names = ['post', 'put', 'delete' ]

  def create(self, request):
    return
  def update(self, request):
    return
  def destroy(self, request):
    return



