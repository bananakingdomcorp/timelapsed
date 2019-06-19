from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from elasticsearch_dsl import Document, Date, Nested, Integer, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text
import datetime

print('yo')

connections.create_connection(alias='elastic_search', hosts=['localhost'], timeout=60)

client = Elasticsearch()

s = Search(using=client)


class Card(Document):
  id = Integer()
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
     name = 'Timelapsed'

  def save(self, ** kwargs):
      return super().save(** kwargs)


Card.init()

