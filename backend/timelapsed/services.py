#Add in services/functionality here

from .models import Users, Topic, Date_Range, Card, Subclass, Card_Relationship_Move_Action, Card_Relationship_Move_Action, Card_Relationship_Delete_Action, Card_Relationship_Subclass_Action, Card_Relationship_In_Same_Action, Subclass_Relationships
from collections import OrderedDict 
from .batching.responses import card_response_builder

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
    same_card = Card.objects.get(id = data['Same']['Card_ID'])
    same_child = Card.objects.get(id = data['Same']['Child_ID'])

    res['id'] = Card_Relationship_In_Same_Action.objects.create(Email = Users.objects.get(Email = user), Card_ID = same_card, Child_ID = same_child ).id
    res['str'] = f'{same_card.Name} must be in the same topic as {same_child.Name}'

    return res

  if 'Delete' in data:
    delete_card = Card.objects.get(id = data['Delete']['Card_ID'])

    res['id'] = Card_Relationship_Delete_Action(Email = Users.objects.get(Email = user), Card_ID = delete_card ).id
    res['str'] = f'{delete_card.Name} is deleted'

    return res

  if 'Subclass' in data:

    subclass_card = Card.objects.get(id = data['Subclass']['Card_ID'])
    subclass = Card.objects.get(id = data['Subclass']['Subclass_ID'])

    res['id'] = Card_Relationship_Subclass_Action(Email = Users.objects.get(Email = user), Card_ID = subclass_card, Subclass_ID = subclass).id
    res['str'] = f'{subclass_card.Name} is added to subclass {subclass.Name}'

    return res



  def peform_child_action(child_action):

    #card_response_builder found in batching/responses. 

    if child_action.Move_ID is not None:

      move_action = child_action.Move_ID
      move_action_card = move_action.Child_ID
      move_action_card.Topic = move_action.Topic_ID
      move_action_card.save()


      #Add to elasticache/response here. 

      card_response_builder.edit(move_action_card)

      return


    if child_action.Delete_ID is not None:

      delete_action = child_action.Delete_ID
      delete_action_card = delete_action.Card_ID
      
      card_response_builder.delete(delete_action_card.id)

      delete_action_card.delete()

      return

    if child_action.Subclass_ID is not None:

      subclass_action = child_action.Subclass_ID
      subclass_action_card = subclass_action.Card_ID
      Subclass_Relationships.objects.create(Email = subclass_action.Email, subclass = subclass_action.Subclass_ID, Child_ID = subclass_action_card)
      
      #Change elasticache/response here. 

      card_response_builder.subclass()

      return 

    if child_action.Tag_ID is not None:

      # Fill in later. 


      pass