from rest_framework.test import APITestCase

from django.contrib.auth.models import User


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

  def test_if_works(self):
    response = self.client.get('/api/subclass/')
    self.assertEqual(response.status_code, 200)