from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships


###### AS THIS IS A TEST THAT WILL HAVE TO BE FREQUENTLY UPDATED TO PRESERVE THE INTEGRITY OF THE DATA MODEL, IT IS IN IT'S OWN FILE


class TestServicesResponses(APITestCase):

  ##Tests the response from our services.py file. 
  
  @classmethod
  def setUpTestData(cls):
    ### setUpTestData sets things once for the entire class ###
    ### Do not use for authentication, can be used for models ###

   Users.objects.create(Email = 'test@test.com')
   Topic.objects.create(Name = 'First_Topic', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
   Topic.objects.create(Name = 'Second_Topic', Position = 2, Email = Users.objects.get(Email = 'test@test.com'))

   
   ##add cards as well as date_times##


  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################

