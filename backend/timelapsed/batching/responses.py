# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache import cache #local caching. 
from ..models import Card, Topic, Date_Range


# Builds card responses.


def edit_builder(card):

  return {'Name' : card.Name, 'Description': card.Description, 'Position': card.Position, 'Topic': Topic.objects.get(id = card.id).id,  'Return_Times' : [j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = card.id)).order_by('Begin_Date') ]   }


class card_response_builder:
  
  @staticmethod
  def edit(info):

    if 'edit' not in cache:
      cache.set('edit', [])


    edits = cache.get('edit')

    if info.id not in edits:
      edits[info.id] = edit_builder(info)

    cache.set('edit', edits)

    return


  @staticmethod
  def delete(id):

    if 'delete' in locmem:
      locmem.set('delete', [])

    deletes = cache.get('delete')

    deletes.append(id)

    cache.set('delete', deletes)

    return

  @staticmethod
  def return_response():


    #Response is built, but then cleared to ensure it doesn't get reused. 
    res = {}

    if 'edit' in cache:
      res['edit'] = cache.get('edit')

    if 'delete' in cache:
      res['delete'] = cache.get('delete')


    cache.clear()    

    return res

