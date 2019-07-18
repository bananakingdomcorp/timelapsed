# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache.backends import locmem #local caching. 


# Builds card responses.

class response_builder:


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

    


  def return_response(self):


    #Response is built, but then cleared to ensure it doesn't get reused. 

    locmem.clear()
    pass
