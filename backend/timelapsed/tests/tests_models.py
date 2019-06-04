### For Database testing

from django.test import TestCase

from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships

class DatabaseProperlyConnectedTest(TestCase):

## This test is just a sanity check to ensure that our database is connected and properly recieving requests. 

  def setUp(self):

    Users.objects.create(Email = '12345@hello.com')

  def test_user_created(self):
    new_user = Users.objects.values('Email').get(Email = '12345@hello.com')

    self.assertEqual(new_user['Email'], '12345@hello.com')



