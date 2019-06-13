from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist

import datetime



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

  # This class tests our post responses without considering our date/times. Use the date_range classes for that. 

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

  def test_for_topic_setup(self):
    #Checks to make sure a topic ID was added
    self.assertNotEqual(self.topic_id, 0)

  def test_if_rejects_get(self):
    response = self.client.get('/api/card/')

    self.assertEqual(response.status_code, 405) 

  def test_if_accepts_post(self):
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')

    self.assertEqual(response.status_code, 201)

  def test_if_rejects_Empty_post(self):
    response = self.client.post('/api/card/', {})

    self.assertEqual(response.status_code, 400) 
  def test_if_rejects_wrong_post_name(self):
    response = self.client.post('/api/card/', {'Data': {'Drame': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')

    self.assertEqual(response.status_code, 400)

  def test_if_post_rejects_invalid_topic(self):
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': 800000}}, format = 'json')

    self.assertEqual(response.status_code, 400)

  def test_if_accepts_put_with_Name(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Name': 'First'}}, format= 'json')

    self.assertEqual(response.status_code, 200)

  def test_if_accepts_put_with_description(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Description': 'Changed'}}, format= 'json')    

    self.assertEqual(response.status_code, 200)

  def test_if_rejects_empty_put(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/{first_id}/', {}, format= 'json')

    self.assertEqual(response.status_code, 400)

  def test_if_put_rejects_invalid_id(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/8000/', {'Data':{'Name': 'First'}}, format= 'json')

    self.assertEqual(response.status_code, 404)

  def test_if_put_rejects_invalid_topic(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Topic': 8000}}, format= 'json')    

    self.assertEqual(response.status_code, 400)

  def test_if_put_accepts_valid_position(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    second = self.client.post('/api/card/', {'Data': {'Name': 'Second', 'Description': 'Tester', 'Topic': self.topic_id}}, format = 'json')
    second_id = decode_response(second)['Data']['id']    

    response = self.client.put(f'/api/card/{second_id}/', {'Data':{'Switch_Position': first_id}}, format= 'json')      

    self.assertEqual(response.status_code, 200)

  def test_if_put_rejects_invalid_position(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']

    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Switch_Position': 8000}}, format= 'json')      

    self.assertEqual(response.status_code, 400)

  def test_if_put_accepts_valid_topic(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']

    switch_topic = Topic.objects.create(Name = 'UseForTesting', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )

    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Switch_Topic': switch_topic.id}}, format= 'json')    

    self.assertEqual(response.status_code, 200)



  def test_if_put_rejects_invalid_topic(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']
    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Switch_Topic': 8000}}, format= 'json')    

    self.assertEqual(response.status_code, 400)
  
  def test_if_put_accepts_own_topic(self):
    #Yes it's dumb, but there may be issues (especially with concurrency) where you may have this situation. 
    #We are going to allow it is it does nothing to harm the product. 
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']


    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Switch_Topic': self.topic_id}}, format= 'json')    

    self.assertEqual(response.status_code, 200)
  
  def test_if_put_accepts_own_position(self):
    #Reasoning is same as above. 
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']


    response = self.client.put(f'/api/card/{first_id}/', {'Data':{'Switch_Position': first_id}}, format= 'json')    

    self.assertEqual(response.status_code, 200)    

  
  def test_if_accepts_delete(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']


    response = self.client.delete(f'/api/card/{first_id}/')    

    self.assertEqual(response.status_code, 204)    


  def test_if_delete_rejects_invalid_id(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']


    response = self.client.delete(f'/api/card/8000/')    

    self.assertEqual(response.status_code, 404)    



class TestCardFunctionality(APITestCase):
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

  def test_for_topic_setup(self):
    #Checks to make sure a topic ID was added
    self.assertNotEqual(self.topic_id, 0)

  def test_card_name_creates_correctly(self):

    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    self.assertEqual(decode_response(response)['Data']['Name'], 'First' )

  def test_card_description_creates_correctly(self):
    
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    self.assertEqual(decode_response(response)['Data']['Description'], 'Test' )    

  def test_card_position_creates_correctly(self):
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json') 
    response_id = decode_response(response)['Data']['id']       
    self.assertEqual( Card.objects.get(id = response_id).Position , 1)

  def test_card_creates_in_proper_topic(self):
    
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json') 
    response_id = decode_response(response)['Data']['id']       
    self.assertEqual( Card.objects.get(id = response_id).Topic , Topic.objects.get(id = self.topic_id))    

  def test_card_updates_name_correctly(self):
    
    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    response_id = decode_response(response)['Data']['id']  

    second =  self.client.put(f'/api/card/{response_id}/', {'Data': {'Name': 'Changed'}}, format = 'json' )

    self.assertEqual(decode_response(second)['Data']['Name'], 'Changed')

  def test_card_updates_description_correctly(self):

    response = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    response_id = decode_response(response)['Data']['id']  

    second =  self.client.put(f'/api/card/{response_id}/', {'Data': {'Description': 'Changed'}}, format = 'json' )

    self.assertEqual(decode_response(second)['Data']['Description'], 'Changed')    

  def test_card_names_not_unique(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'REally_First', 'Topic': self.topic_id}}, format = 'json')
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Second', 'Topic': self.topic_id}}, format = 'json')        
    first_name = decode_response(first)['Data']['Name']      
    second_name = decode_response(second)['Data']['Name']    

    self.assertEqual(first_name, second_name)  

  def test_card_descriptions_not_unique(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    second = self.client.post('/api/card/', {'Data': {'Name': 'Second', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')        
    first_description = decode_response(first)['Data']['Description']      
    second_description = decode_response(second)['Data']['Description']    

    self.assertEqual(first_description, second_description)      


  def test_card_changes_topic_correctly(self):

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']  
    changed_topic =  Topic.objects.create(Name = 'changed', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    self.client.put(f'/api/card/{first_id}/', {'Data': {'Switch_Topic': changed_topic.id}}, format = 'json' ) 

    self.assertEqual(Card.objects.get(id = first_id).Topic, changed_topic)

  def test_card_changes_position_correctly(self):   

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')        
    first_id = decode_response(first)['Data']['id']      
    second_id = decode_response(second)['Data']['id']    
    self.client.put(f'/api/card/{first_id}/', {'Data': {'Switch_Position': second_id}}, format = 'json' )

    self.assertEqual(Card.objects.get(id = first_id).Position, 2)    
  
  def test_card_goes_to_correct_position_when_moved_to_new_topic(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']  
    changed_topic =  Topic.objects.create(Name = 'changed', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': changed_topic.id}}, format = 'json') 
    second_id = decode_response(second)['Data']['id']        
    self.client.put(f'/api/card/{first_id}/', {'Data': {'Switch_Topic': changed_topic.id}}, format = 'json' ) 

    self.assertEqual(Card.objects.get(id = first_id).Position, 2)


  def test_card_goes_to_correct_position_when_topic_and_position_changed(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']  
    changed_topic =  Topic.objects.create(Name = 'changed', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': changed_topic.id}}, format = 'json') 
    second_id = decode_response(second)['Data']['id']        
    self.client.put(f'/api/card/{first_id}/', {'Data': {'Switch_Topic': changed_topic.id, 'Switch_Position': second_id}}, format = 'json' ) 

    self.assertEqual(Card.objects.get(id = first_id).Position, 1)


  def test_if_cards_delete_when_topic_deletes(self):
    to_delete =  Topic.objects.create(Name = 'changed', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': to_delete.id}}, format = 'json') 
    first_id = decode_response(first)['Data']['id']
    self.client.delete(f'/api/topic/{to_delete.id}/')

    with self.assertRaises(ObjectDoesNotExist):
      Card.objects.get(id = to_delete.id)

  def test_card_iterates_highest_position_in_topic(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')
    third = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')
    second_id = decode_response(second)['Data']['id']

    self.client.delete(f'/api/card/{second_id}/')
    fourth = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}}, format = 'json')
    fourth_id = decode_response(fourth)['Data']['id']
    self.assertEqual(Card.objects.get(id = fourth_id).Position, 4)

  def test_card_iterates_highest_position_in_topic_after_move_out(self):
    second_topic =  Topic.objects.create(Name = 'changed', Position = 2, Email = Users.objects.get(Email = 'test@test.com') )
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': second_topic.id}}, format = 'json') 
    first_id = decode_response(first)['Data']['id']
    self.client.put(f'/api/card/{first_id}/', {'Data': {'Switch_Topic': self.topic_id}}, format = 'json'  )
    second = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': second_topic.id}}, format = 'json')
    second_id = decode_response(second)['Data']['id']

    self.assertEqual(Card.objects.get(id = second_id).Position, 1)

  def test_card_deletes_correctly(self):
    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')
    first_id = decode_response(first)['Data']['id']      
    self.client.delete(f'/api/card/{first_id}/')

    with self.assertRaises(ObjectDoesNotExist):
      Card.objects.get(id = first_id)





class TestDateRangeResponses(APITestCase):
  card_setup = 0
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
    card_setup = Card.objects.create(Name = 'Test', Description = 'Test', Position = 1,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.card_id = card_setup.id


    # Day = models.TextField(max_length=100, default = 'Sunday')
    # Begin_Date = models.DateTimeField(default = now)
    # Num_Weeks = models.IntegerField(default = 0)
    # Weeks_Skipped = models.IntegerField(default = 0)
    # Begin_Time = models.TimeField()
    # End_Time = models.TimeField()      

  def test_if_accepts_valid_post(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Saturday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)

  def test_if_rejects_incomplete_post(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 400)    

  
  def test_if_post_rejects_empty_times(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [] }, format = 'json') 
    self.assertEqual(first.status_code, 400)    

  def test_if_rejects_post_without_data(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Times': [{'Day' : 'Saturday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 400)    

  def test_if_accepts_put_without_Data(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [], 'Delete' : [test.id]} }, format = 'json')

    self.assertEqual(response.status_code, 200)

  def test_if_accepts_put_only_edits(self):

    # begin = datetime.datetime(1999, 4, 14)
    # begin_timed = datetime.time(4, 25)
    # end_timed = datetime.time(7, 59)

    # test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    # response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [], 'Delete' : [test.id]} }, format = 'json')

    # self.assertEqual(response.status_code, 200)

    pass

  def test_if_rejects_nonexistent_edits(self):
    pass
  
  def test_if_accepts_put_only_additions(self):
    pass

  def test_if_rejects_incorrect_additions(self):
    pass

  def test_if_accepts_put_only_deletions(self):
    pass

  def test_if_rejects_incorrect_deletions(self):
    pass
  





class TestDateRangeFunctionality(APITestCase):
  card_setup = 0

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
    card_setup = Card.objects.create(Name = 'Test', Description = 'Test', Position = 1,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.card_id = card_setup.id

  def test_if_day_creates_correctly_on_post(self):


    pass
  def test_if_begin_date_creates_correctly(self):
    pass
  def test_if_num_weeks_creates_correctly(self):
    pass
  def test_if_num_weeks_defaults_correctly(self):
    pass
  def test_if_weeks_skipped_creates_correctly(self):
    pass
  def test_if_weeks_skipped_defaults_correctly(self):
    pass
  def test_if_begin_time_creates_correctly(self):
    pass
  def test_if_end_time_creates_correctly(self):
    pass
  def test_if_begin_time_edits_correctly(self):
    pass
  def test_if_end_time_edits_correctly(self):
    pass
  def test_if_num_weeks_edits_correctly(self):
    pass
  def test_if_begin_date_rejects_edit(self):
    #Might be better for responses
    pass
  def test_if_day_rejects_edit(self):
    #Might be better for responses
    pass
  def test_if_times_add_in_put(self):
    pass

  def test_if_times_delete(self):
    pass

  def test_if_times_delete_when_card_deletes(self):
    pass
    

  


  