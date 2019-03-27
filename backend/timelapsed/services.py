#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card

from django.db.models.functions import Cast

import datetime

def get_user_information(data):

  test = [i for i in Topic.objects.values('Name', 'id').filter(Email = data['Email']).order_by('Position') ]

  obj = {}

  for i in test:
    cards = [i for i in Card.objects.values('Name', 'Description', Cast('Expected_Finish', datetime.datetime.strftime('%m/%d/%Y') )).filter(Topic = i['id']).order_by('Position')]
    obj[i['Name']] = cards

  return obj

  