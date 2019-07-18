# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache.backends import locmem #local caching. 


# Builds card responses.

class card_response_builder:


  def __init__(self):
    pass


  def edit(self, info):

    if 'edit' not in locmem.keys():
      locmem.set('edit', [])


    edits = locmem.get('edit')

    edits.append(info)

    locmem.set('edit', edits)

    
    pass


  def delete(self, id):

    if 'delete' not in locmem.keys():
      locmem.set('delete', [])

    deletes = locmem.get('delete')

    deletes.append(id)

    locmem.set('delete', deletes)

    


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