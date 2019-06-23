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




class DateRangeModelTest(TestCase):
  card_id = 0

  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    Topic.objects.create(Name = 'ModelsTest', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    card_setup = Card.objects.create(Name = 'Test', Description = 'Test', Position = 1,  Topic = Topic.objects.get(Name = 'ModelsTest'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.card_id = card_setup.id


  def test_succeds_with_day_Sunday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Sunday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Sunday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Monday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Monday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Monday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Tuesday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Tuesday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Tuesday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Wednesday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Wednesday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Wednesday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Thursday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Thursday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Thursday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Friday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Friday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Friday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_succeds_with_day_Saturday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    self.assertEqual(test.Day, 'Saturday')
    self.assertEqual(test.Begin_Date, begin)
    self.assertEqual(test.Num_Weeks, 0)
    self.assertEqual(test.Weeks_Skipped, 0)
    self.assertEqual(test.Begin_Time, begin_timed)
    self.assertEqual(test.End_Time, end_timed)

  def test_fails_with_invalid_day(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    with self.assertRaises(Exception):
      Date_Range.objects.create(Day = 'invalid', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )
  
  def test_fails_when_incomplete(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    with self.assertRaises(ValidationError):
      Date_Range.objects.create(Day = 'Sunday', Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )  
  




class TestDateRangeResponses(APITestCase):
  card_id = 0
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

  def test_if_accepts_valid_post_Sunday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)


  def test_if_accepts_valid_post_Monday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Monday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)


  def test_if_accepts_valid_post_Tuesday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Tuesday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)    

  def test_if_accepts_valid_post_Wednesday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Wednesday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)


  def test_if_accepts_valid_post_Thursday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)

  def test_if_accepts_valid_post_Friday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Friday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)

  def test_if_accepts_valid_post_Saturday(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Saturday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)


  def test_if_rejects_post_with_invalid_day(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'fdsafkljfjkl', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
   
    self.assertEqual(first.status_code, 400)


  def test_if_post_accepts_multiples_times(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Saturday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, {'Day' : 'Friday', 'Begin_Date' : begin, 'Num_Weeks' : 2, 'Weeks_Skipped' : 4, 'Begin_Time' : begin_timed, 'End_Time' : end_timed} ] }, format = 'json') 
    self.assertEqual(first.status_code, 201)


  def test_if_post_rejects_multiple_times_with_one_incorrect(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Saturday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, {'Day' : 'Flyday', 'Begin_Date' : begin, 'Num_Weeks' : 2, 'Weeks_Skipped' : 4, 'Begin_Time' : begin_timed, 'End_Time' : end_timed} ] }, format = 'json') 
    self.assertEqual(first.status_code, 400)

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

  def test_if_accepts_delete_put(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [], 'Delete' : [test.id]} }, format = 'json')

    self.assertEqual(response.status_code, 200)

  def test_if_accepts_edit_put(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {1: {'Num_Weeks': 1, 'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': test.id }}, 'Add' : [], 'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 200)

  def test_if_rejects_nonexistent_edit_ids(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {1: {'Num_Weeks': 1, 'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': 800000 }}, 'Add' : [], 'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 400)


  def test_if_rejects_incomplete_edit_data(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {
      'Times': {'Edit' : {1: {'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': test.id }},
       'Add' : [],
        'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 400)
  

  def test_if_accepts_put_only_additions(self):
 
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)
 
    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 200)


  def test_if_rejects_incomplete_addition_data(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)
 
    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [{ 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 400)

  def test_if_rejects_invalid_deletions(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': {'Edit' : {}, 'Add' : [], 'Delete' : [8000]} }, format = 'json')

    self.assertEqual(response.status_code, 400)

  def test_if_accepts_deletions_and_additions(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': 
    {'Edit' : {}, 
    'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 
    'Delete' : [test.id]} }, format = 'json')
    self.assertEqual(response.status_code, 200)    

  def test_if_accepts_deletions_and_edits(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    to_delete = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )
    to_edit = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': 
    {'Edit' : {1: {'Num_Weeks': 1, 'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': to_edit.id }},
     'Add' : [],
     'Delete' : [to_delete.id]} }, format = 'json')

    self.assertEqual(response.status_code, 200)    

  def test_if_accepts_additions_and_edits(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    to_edit = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = self.card_id) )

    response = self.client.put(f'/api/card/{self.card_id}/', {'Times': 
    {'Edit' : {1: {'Num_Weeks': 1, 'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': to_edit.id }},
     'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}],
     'Delete' : []} }, format = 'json')

    self.assertEqual(response.status_code, 200)      

  def test_if_rejects_invalid_time(self):
    pass
  



class TestDateRangeFunctionality(APITestCase):
  topic_id = 0  
  card_id = 0

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

  def test_if_day_creates_correctly_on_post(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Day, 'Sunday' )

  def test_if_begin_date_creates_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Begin_Date, begin )


  def test_if_num_weeks_creates_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 1, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Num_Weeks, 1 )


  def test_if_num_weeks_defaults_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Num_Weeks, 0 )



  def test_if_weeks_skipped_creates_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 1, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Weeks_Skipped, 1 )


  def test_if_weeks_skipped_defaults_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 1, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Weeks_Skipped, 0 )


  def test_if_begin_time_creates_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 1, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.Begin_Time, begin_timed )

  def test_if_end_time_creates_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    first = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'test', 'Topic': self.topic_id}, 
    'Times': [{'Day' : 'Sunday', 'Begin_Date' : begin, 'Num_Weeks' : 1, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, ] }, format = 'json') 
    first_id = decode_response(first)['Data']['ids'][0]

    test = Date_Range.objects.get(id = first_id)

    self.assertEqual(test.End_Time, end_timed )

  def test_if_begin_time_edits_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    change_begin_time = datetime.time(5, 19)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']
  
    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = test_card_id)  )


    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {1: {'Num_Weeks': 0, 'Weeks_Skipped' : 0, 'Begin_Time' : change_begin_time, 'End_Time': end_timed, 'id': test.id }}, 'Add' : [], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(int(str.split(next(x['Begin_Time'] for x in times if x['id'] == test.id), ':' )[0]), 5)
    self.assertEqual(int(str.split(next(x['Begin_Time'] for x in times if x['id'] == test.id), ':' )[1]), 19)

  def test_if_end_time_edits_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    change_end_time = datetime.time(12, 47)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']  

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = test_card_id) )


    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {1: {'Num_Weeks': 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time': change_end_time, 'id': test.id }}, 'Add' : [], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(int(str.split(next(x['End_Time'] for x in times if x['id'] == test.id), ':' )[0]), 12)
    self.assertEqual(int(str.split(next(x['End_Time'] for x in times if x['id'] == test.id), ':' )[1]), 47)


  def test_if_num_weeks_edits_correctly(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'),  Card_ID = Card.objects.get(id = test_card_id) )

    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {1: {'Num_Weeks': 99, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time': end_timed, 'id': test.id }}, 'Add' : [], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(next(x['Num_Weeks'] for x in times if x['id'] == test.id), 99)


  def test_if_times_add_in_put(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']

    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {}, 'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(len(times), 1)


  def test_if_multiple_times_add_in_put(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)


    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']

    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {}, 'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, {'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(len(times), 2)



  def test_if_times_delete(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']

    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = test_card_id))

    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {}, 'Add' : [], 'Delete' : [test.id]} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    self.assertEqual(len(times), 0)


  def test_if_times_delete_when_card_deletes(self):
    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']
    
  
    test = Date_Range.objects.create(Day = 'Saturday', Begin_Date = begin, Num_Weeks = 0, Weeks_Skipped = 0, Begin_Time = begin_timed, End_Time = end_timed, Email = Users.objects.get(Email = 'test@test.com'), Card_ID = Card.objects.get(id = test_card_id) )

    self.client.delete(f'/api/card/{test_card_id}/')

    with self.assertRaises(ObjectDoesNotExist):
      Date_Range.objects.get(id = test.id)



  def test_if_dates_return_in_proper_order(self):

    begin = datetime.datetime(1999, 4, 14)
    begin_timed = datetime.time(4, 25)
    end_timed = datetime.time(7, 59)

    begin_earlier =datetime.datetime(1979, 1, 23)

    test_card = self.client.post('/api/card/', {'Data': {'Name': 'First', 'Description': 'Test', 'Topic': self.topic_id}}, format = 'json')    
    test_card_id =  decode_response(test_card)['Data']['id']

    response = self.client.put(f'/api/card/{test_card_id}/', {'Times': {'Edit' : {}, 'Add' : [{'Day': 'Thursday', 'Begin_Date' : begin_earlier, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}, {'Day': 'Thursday', 'Begin_Date' : begin, 'Num_Weeks' : 0, 'Weeks_Skipped' : 0, 'Begin_Time' : begin_timed, 'End_Time' : end_timed}], 'Delete' : []} }, format = 'json')

    times =  decode_response(response)['Data']['Return_Times']

    # Earlier times are less than later times. 


    self.assertLess(times[0]['Begin_Date'],  times[1]['Begin_Date'])

  