#Add in services/functionality here

from .models import Users, Topic, Event, Date_Range, Card

def get_user_information(data):

  test = [i for i in Topic.objects.values('Name', 'id', 'Position').filter(Email = data['Email']).order_by('Position') ]

  obj = {}


  for i in test:
    cards = [i for i in Card.objects.values('Name', 'Description', 'Expected_Finish', 'id' ).filter(Topic = i['id']).order_by('Position')]
    obj[str(i)] = cards

  return obj

  