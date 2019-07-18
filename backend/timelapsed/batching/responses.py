# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache.backends import locmem #local caching. 
from ..models import Card, Topic, Date_Range


# Builds card responses.


def edit_builder(card):

  return {'Name' : card.Name, 'Description': card.Description, 'Position': card.Position, 'Topic': Topic.objects.get(id = card.id).id,  'Return_Times' : [j for j in Date_Range.objects.values('id', 'Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time').filter(Card_ID = Card.objects.get(id = card.id)).order_by('Begin_Date') ]   }

class card_response_builder:


  def __init__(self):
    pass


  def edit(self, info):

    if 'edit' not in locmem.keys():
      locmem.set('edit', [])


    edits = locmem.get('edit')

    if info.id not in edits:
      edits[info.id] = edit_builder(info)

    locmem.set('edit', edits)

    return

  def delete(self, id):

    if 'delete' not in locmem.keys():
      locmem.set('delete', [])

    deletes = locmem.get('delete')

    deletes.append(id)

    locmem.set('delete', deletes)

    return


  def return_response(self):


    #Response is built, but then cleared to ensure it doesn't get reused. 

    Elasticsearch_batching.write()


    locmem.clear()    
    pass


class Elasticsearch_batching:
  def __init__(self):
    pass

  def add(self):
    pass
  def delete(self):
    pass

  def write(self):
    pass