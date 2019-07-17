# This file is desgined for response batching. We need this so that we an update multiple items when we have card chains. 

from searchapp import search #Elasticsearch
from django.core.cache.backends import locmem #local caching. 

class response_builder:


  def __init__(self):
    pass

  def update(self):
    pass

  def subclass(self):
    pass

  def edit(self, card):

    #Reset locmem. 

    edits = locmem.get('edit')


    
    pass

  def delete(self):
    pass

  def subclass(self):
    pass

  def return_response(self):


    #Response is built, but then cleared to ensure it doesn't get reused. 

    locmem.clear()
    pass
