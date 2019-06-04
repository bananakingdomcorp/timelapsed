from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..serializers import UsersSerializer, AddTopicSerializer, CreateCardSerializer, EditTopicSerializer , DeleteTopicSerializer, DeleteCardSerializer, UpdateCardSerializer, CreateSubclassSerializer, TopicRelationshipsSerializer, CardRelationshipsSerializer, EditSubclassSerializer, DeleteSubclassSerializer, GetSubclassSerializer, CreateSubclassRelationshipSerializer 


### In this file we want to ensure that our serializers correctly enforce data types. 


class TestUsersSerializer(APITestCase):

  def setUp(self):
    #Runs before every test


    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('username', 'Pas$w0rd')
    self.client.force_authenticate(user)
    ######################################################

  def tearDown(self):
    #Runs after every test  
    pass

  def test_if_works_with_proper_Email_field(self):
    response = self.client.post('/api/user/', {'Email': 'abc@abc.com'})
    self.assertEqual(response.status_code, 201)

  def test_if_rejects_with_empty_Email_field(self):
    response = self.client.post('/api/user/', {'Email': ''})
    self.assertEqual(response.status_code, 400)

  def test_if_rejects_invalid_Email_field(self):
    response = self.client.post('/api/user/', {'Email': 'fdjlkfsjl'})
    self.assertEqual(response.status_code, 400)

  def test_rejects_with_misnamed_field(self):
    response = self.client.post('/api/user/', {'Dmail': 'test@test.com'})
    self.assertEqual(response.status_code, 400)
  

  

