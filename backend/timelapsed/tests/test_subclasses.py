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


class TestSubclassResponses(APITestCase):
  parent_id = 0
  first_child_id = 0
  topic_id = 0  

  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    parent_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    self.parent_id =  decode_response(parent_card)['Data']['id'] 
    first_child_card = self.client.post('/api/card/', {'Data': {'Name': 'Second', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    self.first_child_id =  decode_response(first_child_card)['Data']['id']    
    ######################################################


  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    set_up_topic = Topic.objects.create(Name = 'UseForTesting', Position = 1, Email = Users.objects.get(Email = 'test@test.com') )
    cls.topic_id = set_up_topic.id

  def test_if_get_rejects_invalid_subclass_id(self):
    response =  self.client.get('/api/subclass/8000/')

    self.assertEqual(response.status_code, 404)

  def test_if_get_accepts_valid_subclass_id(self):
    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

    response = self.client.get(f'/api/subclass/{test.id}/')

    self.assertEqual(response.status_code, 200)


  def test_if_accepts_valid_post(self):

    response = self.client.post('/api/subclass/', {'Head': self.parent_id})

    self.assertEqual(response.status_code, 201)

  def test_if_post_rejects_without_head(self):

    response = self.client.post('/api/subclass/', {'Cards': self.first_child_id})

    self.assertEqual(response.status_code, 400)


  def test_if_post_rejects_with_invalid_head(self):
    pass
  def test_if_post_rejects_with_invalid_children(self):
    pass
  def test_if_put_rejects_with_invalid_pk(self):
    pass
  def test_if_put_accepts_with_valid_information(self):
    pass
  def test_if_put_accepts_with_only_adds(self):
    pass
  def test_if_put_accepts_with_only_deletions(self):
    pass
  def test_if_put_empty(self):
    pass
  def test_if_put_rejects_with_invalid_adds(self):
    pass
  def test_if_put_rejects_with_invalid_deletes(self):
    pass
  def test_if_delete_accepts(self):
    pass
  def test_if_delete_rejects_with_invalid_pk(self):
    pass

  

class TestSubclassFunctionality(APITestCase):
  parent_id = 0
  first_child_id = 0
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
    card_setup = Card.objects.create(Name = 'Parent', Description = 'Parent', Position = 1,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.parent_id = card_setup.id
    child_setup = Card.objects.create(Name = 'First Child', Description = 'First Child', Position = 2,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.first_child_id = child_setup.id

  def test_if_correctly_returns_entire_subclass(self):
    pass
  def test_if_can_find_entire_subclass_from_child(self):
    pass
  def test_if_can_find_entire_subclass_from_head(self):
    pass
  def test_if_correctly_creates_head(self):
    pass
  def test_if_correctly_creates_children(self):
    pass
  def test_if_correctly_adds_on_put(self):
    pass
  def test_if_correctly_deletes_on_put(self):
    pass
  def test_if_fails_when_attempting_to_delete_head(self):
    pass
  def test_if_accepts_add_on_child_already_in_subclass(self):
    pass
  def test_if_correctly_deletes(self):
    pass
  def test_if_correctly_returns_subclass_after_deletion(self):
    pass
  def test_if_subclass_deletes_if_head_removed(self):
    pass

  
  


  

