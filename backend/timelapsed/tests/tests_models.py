### For Database testing

from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships




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



class TopicModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')

  def test_succeeds_with_proper_information(self):
    Topic.objects.create(Name = 'first', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    data = Topic.objects.values('Name', 'Position', 'Email').get(Name = 'first', Position = 1)
    self.assertEquals(data['Name'], 'first')
    self.assertEquals(data['Position'], 1)
    self.assertEquals(data['Email'], 'test@test.com' )


  def test_fails_when_incomplete(self):

    with self.assertRaises(ValidationError):
      Topic.objects.create(Position = 1, Email = Users.objects.get(Email = 'test@test.com'))




class CardModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    Topic.objects.create(Name = 'ModelsTest', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))

  def test_succeds_with_proper_information(self):
    test = Card.objects.create(Name = 'First', Description = 'Test', Position = 1, Email = Users.objects.get(Email = 'test@test.com'), Topic = Topic.objects.get(Name = 'ModelsTest') )
    data = Card.objects.get(Name = 'First', Description = 'Test', Position = 1)
    self.assertEqual(data.Name, 'First' )
    self.assertEqual(data.Description, 'Test')
    self.assertEqual(data.Position, 1)

  def test_fails_when_incomplete(self):
    with self.assertRaises(ValidationError):
      Card.objects.create(Name = 'First', Position = 1, Email = Users.objects.get(Email = 'test@test.com'), Topic = Topic.objects.get(Name = 'ModelsTest') )          

  

  
