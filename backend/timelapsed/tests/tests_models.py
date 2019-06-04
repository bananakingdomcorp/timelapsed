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

  def test_user_does_not_create_when_blank(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = '')

  def test_user_does_not_create_without_email_username(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = '@3fkljf.com')

  def test_user_does_not_create_without_email_domain(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = 'test@')

  def test_user_does_not_create_without_dot_com(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = 'test@3fkljf')

  def test_user_does_not_create_with_invalid_domain(self):

    with self.assertRaises(ValidationError):
      Users.objects.create(Email = 'test@****.com')

  

    








