#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card
from collections import OrderedDict 

def get_user_information(data):

  test = [i for i in Topic.objects.values('Name', 'id').filter(Email = data['Email']).order_by('Position') ]

  arr = []

  arr.append


  for i in test:
    cards = [i for i in Card.objects.values('Name', 'Description', 'id' ).filter(Topic = i['id']).order_by('Position')]
    arr.append( {'Data' : {'id': i['id'], 'Name': i['Name'], 'Cards': cards}} )
    

  return arr

  