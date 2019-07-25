# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache import cache #local caching. 
from ..models import Card, Topic, Date_Range


# Builds card responses.


def edit_builder(card):

  return {'Name' : card.Name, 'Description': card.Description, 'Position': card.Position, 'Topic': card.Topic.id,  'Return_Times' : [j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = card.id)).order_by('Begin_Date') ]   }

def subclass_builder(card):
  return {'Subclass': card.Subclass.id, 'Child_ID': card.Child_ID.id}





class card_response_builder:
  
  @staticmethod
  def edit(info):

    if 'Edit' not in cache:
      cache.set('Edit', {})


    edits = cache.get('Edit')

    if info.id not in edits:
      edits[info.id] = edit_builder(info)

    cache.set('Edit', edits)

    return


  @staticmethod
  def delete(id):

    if 'Delete' not in cache:
      cache.set('Delete', [])

    deletes = cache.get('Delete')

    deletes.append(id)

    cache.set('Delete', deletes)

    return

  @staticmethod
  def subclass_add(info):

    subclass_info = subclass_builder(info)

    if 'Subclass' not in cache:
      cache.set('Subclass', {})

    subclasses = cache.get('Subclass')

    if 'Add' not in subclasses:
      subclasses['Add'] = {}


    if subclass_info['Subclass'] not in subclasses['Add']:
      subclasses['Add'][subclass_info['Subclass']] = [subclass_info['Child_ID']]
    else:
      subclasses['Add'][subclass_info['Subclass']].append(subclass_info['Child_ID'])


    return

  @staticmethod
  def subclass_delete(info):
    #Fill in later

    return


  @staticmethod
  def return_response():


    #Response is built, but then cleared to ensure it doesn't get reused. 
    res = {}

    if 'Edit' in cache:
      res['Edit'] = cache.get('Edit')

    if 'Delete' in cache:
      res['Delete'] = cache.get('Delete')

    if 'Subclass' in cache:
      res['Subclass'] = cache.get('Subclass')


    cache.clear()    

    return res

