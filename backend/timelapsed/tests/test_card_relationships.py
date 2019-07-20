from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from ..models import Users, Topic, Date_Range, Card, Subclass, Topic_Relationships,  Subclass_Relationships, Card_Relationship_Parent_Action, Card_Relationship_Child_Action, Card_Relationship_Move_Action, Card_Relationship_In_Same_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action

from django.test import TestCase

import json

from django.core.exceptions import ObjectDoesNotExist

import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


## Use decode_response do get object payload ##


def decode_response(res):
  d = res.content.decode()
  return json.loads(d)



