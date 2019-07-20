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

    if 'edit' not in cache:
      cache.set('edit', {})


    edits = cache.get('edit')

    if info.id not in edits:
      edits[info.id] = edit_builder(info)

    cache.set('edit', edits)

    return


  @staticmethod
  def delete(id):

    if 'delete' not in cache:
      cache.set('delete', [])

    deletes = cache.get('delete')

    deletes.append(id)

    cache.set('delete', deletes)

    return

  @staticmethod
  def subclass_add(info):

    subclass_info = subclass_builder(info)

    if 'subclass' not in cache:
      cache.set('subclass', {})

    subclasses = cache.get('subclass')

    if 'add' not in subclasses:
      subclasses['add'] = {}


    if subclass_info['Subclass'] not in subclasses['add']:
      subclasses['add'][subclass_info['Subclass']] = [subclass_info['Child_ID']]
    else:
      subclasses['add'][subclass_info['Subclass']].append(subclass_info['Child_ID'])


    return

  @staticmethod
  def subclass_delete(info):
    #Fill in later

    return


  @staticmethod
  def return_response():


    #Response is built, but then cleared to ensure it doesn't get reused. 
    res = {}

    if 'edit' in cache:
      res['edit'] = cache.get('edit')

    if 'delete' in cache:
      res['delete'] = cache.get('delete')

    if 'subclass' in cache:
      res['subclass'] = cache.get('subclass')


    cache.clear()    

    return res

