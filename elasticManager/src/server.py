import logging
from datetime import date

from elasticsearch import Elasticsearch, BadRequestError
from flask import Flask, request


class Server:
    def __init__(self, host, port, db_client, elastic_url):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.db_client = db_client
        self.elastic_client = Elasticsearch(elastic_url, verify_certs=False)
        if not self.elastic_client.ping():
            raise ValueError("Connection failed")
        self.set_routes()
        a = self._handle_get()

        self.index_branches()
        collection = db_client['Products']
        cursor = collection.find({})
        if not cursor:
            raise ValueError("MONGO NO DATA LPMQLP")
        for document in cursor:
            print(document)
        collection = db_client['Prices']
        cursor = collection.find({})
        if not cursor:
            raise ValueError("MONGO NO DATA LPMQLP")
        for document in cursor:
            print(document)
        print(a)

    def set_routes(self):
        try:
            self.app.add_url_rule('/', view_func=self._handle_get, methods=['GET'])
            self.app.add_url_rule('/', view_func=self._handle_post, methods=['POST'])
        except Exception as error:
            print(error)
            logging.error("Could not set routes")

    def _handle_get(self):
        return {"status": "OK"}

    def _handle_post(self):
        data = request.get_json()
        response = {"message": "unmensajin"}
        return response

    def close(self):
        pass

    def index_branches(self):
        request_body = {
            "settings" : {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },

            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "branch": {"type": "text"},
                    "address": {"type": "text"},
                    "location": {"type": "geo_point"},
                }
            }
        }
        print("creating 'branches' index...")
        try:
            resp = self.elastic_client.indices.create(index = 'branches', body = request_body)
            print (resp)
        except BadRequestError as e:
            print(e.info)

        collection = self.db_client['Branches']
        print("Querying info")
        cursor = collection.find({})
        if not cursor:
            raise ValueError("MONGO NO DATA LPMQLP")
        else:
            for doc in cursor:
                print(doc)

        #resp = self.elastic_client.index(index="branches", id=1, document)
        #print("Index result: ", resp['result'])

    def run(self):
        print(f"running {self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port, debug=True)
