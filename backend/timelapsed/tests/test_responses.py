from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist



### NOTE: MIGRATE TO get_object_or_404 when searching for an item in the serializers ###

## Use decode_response do get object payload ##

def decode_response(res):
  d = res.content.decode()
  return json.loads(d)


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

class TestTopicResponses(APITestCase):

  def setUp(self):

    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################
    Users.objects.create(Email = 'test@test.com')    


  def tearDown(self):
    Topic.objects.all().delete()    
    #clears the test database after every test. 


  def test_if_rejects_get(self):
    response = self.client.get('/api/topic/')
    self.assertEqual(response.status_code, 405)

  def test_if_accepts_put(self):
    pk = Topic.objects.create(Name = 'first', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    response = self.client.put(f'/api/topic/{pk.id}/', {'Name': 'Changed'})
    self.assertEqual(response.status_code, 200)

  def test_if_rejects_put_for_invalid_id(self):
    response = self.client.put(f'/api/topic/80000/', {'Name': 'Exist'})
    self.assertEqual(response.status_code, 404)

  def test_if_rejects_put_for_deleted_id(self):
    #checks to ensure that the put can be found originally. 
    pk = Topic.objects.create(Name = 'first', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    response = self.client.put(f'/api/topic/{pk.id}/', {'Name': 'Changed'})
    self.assertEqual(response.status_code, 200)    

    #Then deletes out the item, and checks to ensure 404. 
    Topic.objects.get(id = pk.id).delete()
    test = self.client.put(f'/api/topic/{pk.id}/', {'Name': 'Test'})
    self.assertEqual(test.status_code, 404)

  def test_if_rejects_put_for_wrong_name(self):
    pk = Topic.objects.create(Name = 'first', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    response = self.client.put(f'/api/topic/{pk.id}/', {'Dame': 'Changed'})  
    self.assertEqual(response.status_code, 400)

  def test_if_rejects_put_for_invalid_switchPosition(self):
    pk = Topic.objects.create(Name = 'first', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    response = self.client.put(f'/api/topic/{pk.id}/', {'switchPosition':f'{pk.id + 1}' })      
    self.assertEqual(response.status_code, 404)

  def test_if_rejects_post_for_non_charfield(self): 
    response = self.client.post('/api/topic/', {'Name': []})
    self.assertEqual(response.status_code, 400)

  def test_if_rejects_post_for_incorrect_name(self):
    response = self.client.post('/api/topic/', {'Dame': 'First'})
    self.assertEqual(response.status_code, 400)

  def test_if_accepts_post(self):
    response = self.client.post('/api/topic/', {'Name': 'Second'} )
    self.assertEqual(response.status_code, 201)
 
  def test_if_accepts_delete(self):
    pk = Topic.objects.create(Name = 'second', Position = 2,  Email = Users.objects.get(Email = 'test@test.com') )
    response = self.client.delete(f'/api/topic/{pk.id}/')
    self.assertEqual(response.status_code, 204)

  def test_if_rejects_delete_for_invalid_id(self):
    response = self.client.delete(f'/api/topic/80000/')
    self.assertEqual(response.status_code, 404)    




class TestTopicFunctionality(APITestCase):

  def setUp(self):

    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################
    Users.objects.create(Email = 'test@test.com')    


  def tearDown(self):
    Topic.objects.all().delete()    
    #clears the test database after every test. 

  def test_post_correctly_creates_topic_name(self):
    response = self.client.post('/api/topic/', {'Name': 'Testing'})
    self.assertEqual(decode_response(response)['Data']['Name'], 'Testing')

  def test_post_creates_topic_position(self):
    response = self.client.post('/api/topic/', {'Name': 'Testing'})    
    temp = Topic.objects.get(id = decode_response(response)['Data']['id'])
    ### As of now, position is not returned ###

    self.assertEqual(temp.Position, 1)

  def test_post_correctly_iterates_position(self):
    self.client.post('/api/topic/', {'Name': 'Testing'})    
    response = self.client.post('/api/topic/', {'Name': 'Two'})    
    temp = Topic.objects.get(id = decode_response(response)['Data']['id'])  
    self.assertEqual(temp.Position, 2)  

  def test_post_creates_card_list(self):
    response = self.client.post('/api/topic/', {'Name': 'Testing'})
    temp = decode_response(response)['Data']
    self.assertEqual(type(temp['Cards']), list)

  def test_post_creates_empty_cards_list(self):
    response = self.client.post('/api/topic/', {'Name': 'Testing'})
    temp = decode_response(response)['Data']
    self.assertEqual(len(temp['Cards']), 0)

  def test_put_correctly_changes_name(self):
    first = self.client.post('/api/topic/', {'Name': 'Testing'})    
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/topic/{first_id}/', {'Name': 'Changed'})
    self.assertEqual(Topic.objects.get(id = first_id).Name, 'Changed')

  def test_put_correctly_changes_position(self):
    first = self.client.post('/api/topic/', {'Name': 'First'})  
    second = self.client.post('/api/topic/', {'Name': 'Second'})

    ### First checks to verify the positions are correct. 

    first_id = decode_response(first)['Data']['id']
    second_id = decode_response(second)['Data']['id']

    self.assertEqual(Topic.objects.get(id = first_id).Position, 1)
    self.assertEqual(Topic.objects.get(id = second_id).Position, 2)

    ## Switch the two. 

    response = self.client.put(f'/api/topic/{first_id}/', {'switchPosition': second_id})

    self.assertEqual(Topic.objects.get(id = first_id).Position, 2)
    self.assertEqual(Topic.objects.get(id = second_id).Position, 1)
    

  def test_put_correctly_changes_name_and_position(self):
    first = self.client.post('/api/topic/', {'Name': 'First'})  
    second = self.client.post('/api/topic/', {'Name': 'Second'})

    ### First checks to verify the positions and names are correct. 

    first_id = decode_response(first)['Data']['id']
    second_id = decode_response(second)['Data']['id']

    self.assertEqual(Topic.objects.get(id = first_id).Position, 1)
    self.assertEqual(Topic.objects.get(id = second_id).Position, 2)

    ## Switch the two. 

    response = self.client.put(f'/api/topic/{first_id}/', {'Name': 'Changed', 'switchPosition': second_id})

    # Check to make sure the positions have switched

    self.assertEqual(Topic.objects.get(id = first_id).Position, 2)
    self.assertEqual(Topic.objects.get(id = second_id).Position, 1)

    # Check to make sure the name has changed as well. 
    self.assertEqual(Topic.objects.get(id = first_id).Name, 'Changed')


  def test_delete_properly_deletes_topic(self):

    first = self.client.post('/api/topic/', {'Name': 'First'})  

    first_id = decode_response(first)['Data']['id']

    self.client.delete(f'/api/topic/{first_id}/')

  #Confirms object is deleted. 

    with self.assertRaises(ObjectDoesNotExist):
      Topic.objects.get(id = first_id)


  def test_post_reuses_position_after_deletion(self):

    first =  self.client.post('/api/topic/', {'Name': 'First'})  
    first_id = decode_response(first)['Data']['id']
    self.client.delete(f'/api/topic/{first_id}/')
    second = self.client.post('/api/topic/', {'Name': 'Second'})
    second_id = decode_response(second)['Data']['id']
    self.assertEqual(Topic.objects.get(id = second_id).Position, 1)            


  def test_post_properly_iterates_highest_position_with(self):
    first =  self.client.post('/api/topic/', {'Name': 'First'})  
    second = self.client.post('/api/topic/', {'Name': 'Second'})
    third = self.client.post('/api/topic/', {'Name': 'Third'})

    second_id = decode_response(second)['Data']['id']

    self.client.delete(f'/api/topic/{second_id}')

    fourth = self.client.post('/api/topic/', {'Name': 'Fourth'})

    self.assertEqual(Topic.objects.get(id = decode_response(fourth)['Data']['id'] ).Position, 4)


  def test_post_allows_for_name_reuse(self):
    first =  self.client.post('/api/topic/', {'Name': 'First'})  
    second = self.client.post('/api/topic/', {'Name': 'First'})


    self.assertEqual(Topic.objects.get(id = decode_response(first)['Data']['id']).Name, Topic.objects.get(id = decode_response(second)['Data']['id']).Name  )

  def test_put_allows_for_name_reuse(self):
    first =  self.client.post('/api/topic/', {'Name': 'First'})  
    second = self.client.post('/api/topic/', {'Name': 'Second'})
    second_id = decode_response(second)['Data']['id']

    self.client.put(f'/api/topic/{second_id}/', {'Name': 'First'})
    
    self.assertEqual(Topic.objects.get(id = decode_response(first)['Data']['id']).Name, Topic.objects.get(id = second_id).Name  )

### Add test to ensure that all cards delete when a topic deletes. 



class TestCardResponses(APITestCase):


  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################


  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')



class TestCardFunctionality(APITestCase):

  def setUp(self):

    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('test@test.com', 'test@test.com')
    self.client.force_authenticate(user)
    ######################################################
    Users.objects.create(Email = 'test@test.com')    
  
  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')






  # Add under cards. 
  # def test_if_cards_delete_when_topic_deletes(self):
  #   pass
