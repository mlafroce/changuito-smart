import logging
from datetime import date

from elasticsearch import Elasticsearch
from flask import Flask, request


class Server:
    def __init__(self, host, port, db_client, elastic_url):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.db_client = db_client
        self.elastic_client = Elasticsearch(elastic_url)
        self.set_routes()
        self._handle_get()

    def set_routes(self):
        try:
            self.app.add_url_rule('/', view_func=self._handle_get, methods=['GET'])
            self.app.add_url_rule('/', view_func=self._handle_post, methods=['POST'])
        except Exception as error:
            print(error)
            logging.error("Could not set routes")

    def _handle_get(self):
        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': date.today(),
        }
        resp = self.elastic_client.index(index="test-index", id=1, document=doc)
        print(resp['result'])

        resp = self.elastic_client.get(index="test-index", id=1)
        print(resp['_source'])

        self.elastic_client.indices.refresh(index="test-index")
        resp = self.elastic_client.search(index="test-index", query={"match_all": {}})
        print("Got %d Hits:" % resp['hits']['total']['value'])
        for hit in resp['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        return {"status": "OK"}

    def _handle_post(self):
        data = request.get_json()
        response = {"message": "unmensajin"}
        return response

    def close(self):
        pass

    def run(self):
        self.app.run(host=self.host, port=self.port)
