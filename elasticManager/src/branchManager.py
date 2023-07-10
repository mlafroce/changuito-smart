from elasticsearch import BadRequestError, NotFoundError

BRANCH_MAPPING = {
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

class BranchManager:
    def __init__(self, elastic_client, db_client):
        self.elastic_client = elastic_client
        self.db_client = db_client

    def assert_index(self):
        try:
            resp = self.elastic_client.indices.get(index = 'branches')
        except NotFoundError as e:
            self._create_index()

    def index_documents(self):
        collection = self.db_client['Branches']
        cursor = collection.find({})
        if not cursor:
            raise ValueError("MongoDB cursor failed")
        else:
            for branch in cursor:
                del(branch["_id"])
                self.elastic_client.index(index="branches", id=None, body=branch)

    def _create_index(self):
        try:
            resp = self.elastic_client.indices.create(index = 'branches', body = BRANCH_MAPPING)
        except BadRequestError as e:
            print(e.info)
