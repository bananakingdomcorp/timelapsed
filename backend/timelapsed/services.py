#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card
from collections import OrderedDict 

def get_user_information(data):

  test = [i for i in Topic.objects.values('Name', 'id').filter(Email = data['Email']).order_by('Position') ]

  obj = OrderedDict()

  #Using an ordered Dictionary lets you get more from having a positional element. 


  for i in test:
    cards = [i for i in Card.objects.values('Name', 'Description', 'Expected_Finish', 'id' ).filter(Topic = i['id']).order_by('Position')]
    obj[str(i)] = cards

  return obj

  