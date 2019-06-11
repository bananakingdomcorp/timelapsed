### For Database testing

from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Users, Topic, Date_Range, Card, Subclass, Card_Relationships, Topic_Relationships,  Subclass_Relationships
import datetime



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

  

  
class DateRangeModelTest(TestCase):
  card_id = 0

  @classmethod
  def setUpTestData(cls):
    Users.objects.create(Email = 'test@test.com')
    Topic.objects.create(Name = 'ModelsTest', Position = 1, Email = Users.objects.get(Email = 'test@test.com'))
    card_setup = Card.objects.create(Name = 'Test', Description = 'Test', Position = 1,  Topic = Topic.objects.get(Name = 'ModelsTest'), Email = Users.objects.get(Email = 'test@test.com'))
    cls.card_id = card_setup.id

    # Day = models.TextField(max_length=100, default = 'Sunday')
    # Begin_Date = models.DateTimeField(default = now)
    # Num_Weeks = models.IntegerField(default = 0)
    # Weeks_Skipped = models.IntegerField(default = 0)
    # Begin_Time = models.TimeField()
    # End_Time = models.TimeField()        


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
  


  
  
