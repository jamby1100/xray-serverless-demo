import os

from elasticsearch import Elasticsearch

class ElasticsearchGateway:

    @classmethod
    def search_index(cls, index_name, query):
        es = Elasticsearch(
            [os.getenv("ELASTICSEARCH_HOST")],
            http_auth=(os.getenv('ELASTICSEARCH_USER'), os.getenv('ELASTICSEARCH_PASSWORD')),
            scheme="https",
            port=443,
        )
            
        search_result = es.search(index=index_name, body=query)   

        return search_result         