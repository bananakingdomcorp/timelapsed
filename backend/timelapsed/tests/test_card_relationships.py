from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Topic_Relationships,  Subclass_Relationships, Card_Relationship_Parent_Action, Card_Relationship_Child_Action, Card_Relationship_Move_Action, Card_Relationship_In_Same_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist

import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


## Use decode_response do get object payload ##


def decode_response(res):
  d = res.content.decode()
  return json.loads(d)



class TestCardRelationshipResponses(APITestCase):
  parent_id = 0
  first_child_id = 0
  first_topic_id = 0  
  second_topic_id = 1

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
    set_up_second_topic = Topic.objects.create(Name = 'UseForTesting2', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    cls.second_topic_id = set_up_second_topic.id

  def test_if_rejects_empty_parent_post(self):
    
    response = self.client.post('/api/card_relationship/', {'Child_Action': {'Delete': {'Card_ID': self.parent_id}}}, format = 'json')

    self.assertEqual(response.status_code, 400)

  
  def test_if_rejects_multiple_parent_relationships(self):
    
    response = self.client.post('/api/card_relationship/', {'Parent_Action': {'Move': {'Card_ID' : self.first_child_id, 'Topic_ID' : self.second_topic_id}, 'Delete': {'Card_ID': self.first_child_id} }, 'Child_Action': {'Delete': {'Card_ID': self.parent_id}}}, format = 'json')

    self.assertEqual(response.status_code, 400)


  def test_if_accepts_moves(self):
    pass
  def test_if_accepts_valid_parent_same(self):
    pass
  def test_if_accepts_valid_deletes(self):
    pass
  def test_if_accepts_valid_subclasses(self):
    pass
  def test_if_rejects_same_with_child_actions(self):
    pass
  def test_if_rejects_multiple_child_relationships(self):
    pass
  def test_if_rejects_empty_child_actions(self):
    pass
  def test_if_rejects_with_only_child(self):
    pass
  def test_if_rejects_actions_on_same_card(self):
    pass
  def test_if_move_rejects_with_invalid_card_id(self):
    pass
  def test_if_move_rejects_with_invalid_topic_id(self):
    pass
  def test_if_same_rejects_with_invalid_card_id(self):
    pass
  def test_if_same_rejects_with_invalid_child_id(self):
    pass
  def test_if_same_rejects_if_child_and_card_are_same(self):
    pass
  def test_if_delete_rejects_with_invalid_card_id(self):
    pass
  def test_if_subclass_rejects_with_invalid_card_id(self):
    pass
  def test_if_subclass_rejects_with_invalid_subclass_id(self):
    pass




class TestCardRelationshipFunctionality(APITestCase):
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

  def test_if_properly_creates_move_relationship(self):
    pass
  def test_if_properly_creates_same_relationship(self):
    pass
  def test_if_properly_creates_subclass_relationship(self):
    pass
  def test_if_properly_moves_child_card(self):
    pass
  def test_if_deletes_same_if_either_card_is_deleted(self):
    pass
  
  
