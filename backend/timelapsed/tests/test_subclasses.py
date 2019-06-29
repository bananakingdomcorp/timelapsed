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

    response = self.client.post('/api/subclass/', {'Head': 85000})

    self.assertEqual(response.status_code, 400)


  def test_if_post_rejects_with_invalid_children(self):

    response = self.client.post('/api/subclass/', {'Head': self.parent_id, 'Cards': 85000000})    
    
    self.assertEqual(response.status_code, 400)


  def test_if_put_rejects_with_invalid_pk(self):
    
    response = self.client.put('/api/subclass/80000000/')

    self.assertEqual(response.status_code, 400)

  def test_if_put_accepts_with_only_adds(self):
    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )


    print(test.id, 'GISAOFJLKDSFJSIOA')

    response = self.client.put(f'/api/subclass/{test.id}/', {'Add' : [ self.first_child_id ]})

    self.assertEqual(response.status_code, 200)


  def test_if_put_accepts_with_only_deletions(self):

    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

    relationship = Subclass_Relationships.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Subclass = Subclass.objects.get(id = test.id), Child_ID = Card.objects.get(id = self.first_child_id))
    
    response = self.client.put(f'/api/subclass/{test.id}/', {'Remove' : [self.first_child_id]})

    self.assertEqual(response.status_code, 200)

  def test_if_rejects_empty_put(self):

    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

    response = self.client.put(f'/api/subclass/{test.id}/', {})

    self.assertEqual(response.status_code, 400 )


  def test_if_put_rejects_with_invalid_adds(self):

    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

    response = self.client.put(f'/api/subclass/{test.id}/', {'Add': [90000000]})

    self.assertEqual(response.status_code, 400 )


  def test_if_put_rejects_with_invalid_deletes(self):
  
    test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

    response = self.client.put(f'/api/subclass/{test.id}/', {'Remove': [90000000]})

    self.assertEqual(response.status_code, 400 ) 

  # def test_if_delete_accepts(self):

  #   test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

  #   response = self.client.delete(f'/api/subclass/{test.id}/')  

  #   self.assertEqual(response.status_code, 204)

  # def test_if_delete_rejects_with_invalid_pk(self):

  #   test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )

  #   response = self.client.delete(f'/api/subclass/8000000/')  

  #   self.assertEqual(response.status_code, 400)

  



class TestSubclassFunctionality(APITestCase):
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

  def test_if_correctly_creates_head(self):
    


    
    pass
  def test_if_correctly_creates_children(self):
    pass

  def test_if_get_correctly_returns_entire_subclass(self):

    # test = Subclass.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Head = Card.objects.get(id = self.parent_id) )


    # Subclass_Relationships.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Subclass = Subclass.objects.get(id = test.id), Child_ID = Card.objects.get(id = first_child_id))
    # second_child_card = self.client.post('/api/card/', {'Data': {'Name': 'Third', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    # second_child_id =  decode_response(second_child_card)['Data']['id']   
    # Subclass_Relationships.objects.create(Email = Users.objects.get(Email = 'test@test.com'), Subclass = Subclass.objects.get(id = test.id), Child_ID = Card.objects.get(id = second_child_id))        

    # response = self.client.get(f'/api/subclass/{test.id}/')
    # response_data =  decode_response(response)['Data']['res']     

    # self.assertEqual(response_data, [first_child_id, second_child_id])
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

  def test_if_does_not_add_a_second_subclass_relationship_when_given_existing_relationship(self):
    pass

  
  


  

