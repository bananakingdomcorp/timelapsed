#Add in services/functionality here

from .models import Users, Topic, Date_Range, Card, Card_Relationship_Move_Action, Card_Relationship_Move_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action 
from collections import OrderedDict 

def get_user_information(data):

  test = [i for i in Topic.objects.values('Name', 'id').filter(Email = data['Email']).order_by('Position') ]

  arr = []

  arr.append


  for i in test:
    cards = [i for i in Card.objects.values('Name', 'Description', 'id' ).filter(Topic = i['id']).order_by('Position')]
    for j in cards:
      times = [j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = j['id'])).order_by('Begin_Date') ]
      j['Times'] = times

    arr.append( {'Data' : {'id': i['id'], 'Name': i['Name'], 'Cards': cards}} )
    

  return arr



def create_card_relationship(data):

  if 'Move' in data:

    


    return
  if 'Same' in data:

    return
  if 'Delete' in data:

    return
  if 'Subclass' in data:

    return

  return