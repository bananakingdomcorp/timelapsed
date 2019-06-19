from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch


connections.create_connection(alias='elastic_search', hosts=['localhost'], timeout=60)