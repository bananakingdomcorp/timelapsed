from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from timelapsed.models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist

import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your tests here.


## Use decode_response do get object payload ##

def decode_response(res):
  d = res.content.decode()
  return json.loads(d)



class TestCardElasticSearch(APITestCase):
  topic_id = 0

  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################


  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    set_up_topic = Topic.objects.create(Name = 'UseForTesting', Position = 1, Email = Users.objects.get(Email = 'test@test.com') )
    cls.topic_id = set_up_topic.id

  def test_if_creates_on_id(self):


    pass
  def test_if_creates_properly(self):
    
    
    pass
  def test_if_creates_suggestions_for_name(self):
    
    
    pass
  def test_if_creates_suggestions_for_descriptio(self):
    
    
    pass
  def test_if_creates_suggestions_for_topic(self):
    
    
    pass
  def test_if_deletes_properly(self):
    
    
    pass
  def test_if_updates_properly(self):
    
    
    pass
  