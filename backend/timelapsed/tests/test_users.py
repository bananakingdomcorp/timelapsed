from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist

import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships


## Use decode_response do get object payload ##

def decode_response(res):
  d = res.content.decode()
  return json.loads(d)

class UserModelTest(TestCase):

## This test is just a sanity check to ensure that our database is connected and properly recieving requests. 

  def test_user_creates_with_Email(self):
    Users.objects.create(Email = '12345@hello.com')

    new_user = Users.objects.values('Email').get(Email = '12345@hello.com')

    self.assertEqual(new_user['Email'], '12345@hello.com')

  def test_user_does_not_create_without_Email(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = 'test')

  def test_user_does_not_create_when_incorrect(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = '')





class TestUsersResponses(APITestCase):


  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################


  def tearDown(self):
    #Runs after every test
    pass

  def test_if_rejects_get(self):
    response = self.client.get('/api/user/')
    self.assertEqual(response.status_code, 405)
  
  def test_if_rejects_put(self):
    response = self.client.put('/api/user/')
    self.assertEqual(response.status_code, 405)

  def test_if_rejects_delete(self):
    response = self.client.delete('/api/user/')
    self.assertEqual(response.status_code, 405)

  def test_if_accepts_post(self):
    response = self.client.post('/api/user/', {'Email' : 'Test@test.com'})
    self.assertEqual(response.status_code, 201)

  def test_if_returns_200_when_valid(self):
    Users.objects.create(Email = 'Test@test.com')
    self.client.post('/api/user/', {'Email' : 'Test@test.com'}, format = 'json')    
    response = self.client.post('/api/user/', {'Email' : 'Test@test.com'}, format = 'json')
    self.assertEqual(response.status_code, 200)

    ### The services response that we get here is found in test_services.py





