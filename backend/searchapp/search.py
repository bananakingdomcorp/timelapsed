from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

from elasticsearch_dsl import Document, Date, Nested, Integer, Boolean, analyzer, InnerDoc, Completion, Keyword, Text, Index,  connections, Search
import datetime

connections.create_connection(alias='default', hosts=['localhost'], timeout = 60)


#### NOTE: ELASTICSEARCH ID SHOULD BE THE SAME AS THE ID USED BY POSTGRES ####

class ElasticSearchCard(Document):
  Name = Text()
  Name_Suggest = Completion()
  Description = Text()
  Description_Suggest = Completion()
  Topic = Text()
  Topic_Suggest = Completion()

  category = Text(
    analyzer='snowball',
    fields={'raw': Keyword()}
  )

  class Index:
     name = 'timelapsed'

  def save(self, ** kwargs):
      return super().save(** kwargs)

  def delete(self, ** kwargs):

    # Fix me. 
      return super().delete(** kwargs)

ElasticSearchCard.init()