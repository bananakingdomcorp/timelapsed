#Add in services/functionality here

from .models import Users, Topic, Date_Range, Card, Subclass, Card_Relationship_Move_Action, Card_Relationship_Move_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action, Card_Relationship_In_Same_Action
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



def create_card_relationship(data, user):
  
  res = {}



  if 'Move' in data:

    move_topic = Topic.objects.get(id = data['Move']['Topic_ID'])
    move_card = Card.objects.get(id = data['Move']['Card_ID'])

    res['id'] = Card_Relationship_Move_Action.objects.create(Email = Users.objects.get(Email = user), Card_ID = move_card, Topic_ID = move_topic )
    res['str'] = f'{move_card.Name} is moved to {move_topic.Name}'

    return res


  if 'Same' in data:

    
    return Card_Relationship_In_Same_Action.objects.create(Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = data['Same']['Card_ID']), Child_ID = Card.objects.get(id = data['Same']['Child_ID']) )

  if 'Delete' in data:

    return Card_Relationship_Delete_Action(Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = data['Delete']['Card_ID']))

  if 'Subclass' in data:

    return Card_Relationship_Subclass_Action(Email = Users.objects.get(Email = user), Card_ID = Card.objects.get(id = data['Subclass']['Card_ID']), Subclass_ID = Subclass.objects.get(id = data['Subclass']['Subclass_ID']))
