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
    ######################################################


  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    set_up_topic = Topic.objects.create(Name = 'UseForTesting', Position = 1, Email = Users.objects.get(Email = 'test@test.com') )
    cls.topic_id = set_up_topic.id
    card_setup = Card.objects.create(Name = 'Parent', Description = 'Parent', Position = 1,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.parent_id = card_setup.id
    child_setup = Card.objects.create(Name = 'First Child', Description = 'First Child', Position = 2,  Topic = Topic.objects.get(Name = 'UseForTesting'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.first_child_id = child_setup.id

  def test_if_get_rejects_invalid_subclass_id(self):
    pass
  def test_if_get_accepts_valid_subclass_id(self):
    pass
  def test_if_accepts_valid_post(self):
    pass
  def test_if_rejects_without_head(self):
    pass
  def test_if_accepts_with_only_head(self):
    pass
  def tet_if_rejects_with_invalid_head(self):
    pass
  




