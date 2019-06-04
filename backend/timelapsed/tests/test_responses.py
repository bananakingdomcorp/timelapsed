from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

class TestUsersResponses(APITestCase):


  def setUp(self):
    #Runs before every test

    ###USE THE FOLLOWING BOILERPLATE BEFORE EVERY REQUEST###
    user = User.objects.create_user('username', 'Pas$w0rd')
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

  def test_if_rejects_bad_request(self):
    response = self.client.post('/api/user/', {'Email' : 'dafjkldfjlk'})
    self.assertEqual(response.status_code, 400)    

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
    user = User.objects.create_user('username', 'Pas$w0rd')
    self.client.force_authenticate(user)
    ######################################################


  def tearDown(self):
    #Runs after every test
    pass


  def test_if_rejects_get(self):
    response = self.client.get('/api/topic/')
    self.assertEqual(response.status_code, 405)

  def test_if_accepts_put(self):
    pass
  
  def test_if_accepts_post(self):
    pass
  
  def test_if_accepts_delete(self):
    pass
  

  